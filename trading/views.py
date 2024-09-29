from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Trade
from django.core.exceptions import ValidationError
from decimal import Decimal

def home(request):
    return render(request, 'trading/home.html')

@login_required
def dashboard(request):
    return render(request, 'trading/dashboard.html')

@login_required
def available_assets(request):
    # In a real application, you would fetch this data from the Deriv API
    assets = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'BTC/USD']
    return render(request, 'trading/available_assets.html', {'assets': assets})

@login_required
def place_trade(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValidationError("Amount must be positive")
            if len(symbol) > 10:
                raise ValidationError("Invalid symbol")
            # Here you would interact with the Deriv API to place the trade
            # For now, we'll just create a Trade object
            Trade.objects.create(user=request.user, symbol=symbol, amount=amount)
            return redirect('trade_history')
        except (ValidationError, ValueError) as e:
            return render(request, 'trading/place_trade.html', {'error': str(e)})
    return render(request, 'trading/place_trade.html')

@login_required
def trade_history(request):
    trades = Trade.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'trading/trade_history.html', {'trades': trades})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'trading/register.html', {'form': form})
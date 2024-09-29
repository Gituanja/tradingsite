from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assets/', views.available_assets, name='available_assets'),
    path('trade/', views.place_trade, name='place_trade'),
    path('history/', views.trade_history, name='trade_history'),
    path('register/', views.register, name='register'),
]
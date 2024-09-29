# trading/utils.py
import requests
import json

API_URL = "https://api.deriv.com/api/v3/"
API_KEY = "YOUR_API_KEY_HERE"

def get_price_proposal(symbol, contract_type, amount):
    payload = {
        "proposal": 1,
        "amount": amount,
        "basis": "stake",
        "contract_type": contract_type,
        "currency": "USD",
        "symbol": symbol
    }
    
    headers = {
        "Content-Type": "application/json",
        "App-ID": API_KEY
    }

    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
    return response.json()

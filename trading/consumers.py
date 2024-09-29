import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import random

class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == 'get_prices':
            await self.send_prices()

    async def send_prices(self):
        # In a real application, you would fetch real-time prices from an API
        # For this example, we'll generate random prices
        prices = {
            'EUR/USD': round(random.uniform(1.0, 1.5), 4),
            'GBP/USD': round(random.uniform(1.2, 1.7), 4),
            'USD/JPY': round(random.uniform(100, 150), 2),
            'BTC/USD': round(random.uniform(30000, 60000), 2)
        }

        await self.send(text_data=json.dumps({
            'type': 'price_update',
            'prices': prices
        }))
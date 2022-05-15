import asyncio
import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async




class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        
     


    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Hello world!")
        await self.send(bytes_data="Hello world!")
      
        await self.close()
        await self.close(code=4123)

    async def disconnect(self, close_code):
        print(close_code)
    
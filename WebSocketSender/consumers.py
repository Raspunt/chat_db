import asyncio
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer





class ChatConsumer(AsyncJsonWebsocketConsumer):

    jsonMessage = ""
    MessageSended = False
    
    async def connect(self):
        
        await self.channel_layer.group_add(
            'chat_online',
            self.channel_name
        )
        await self.accept()


        # await self.send(self.josnMessage)

        
    async def events_alarm(self,event):
         await self.send_json({
                'content': event['content']
            })





    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Hello world!")
        await self.send(bytes_data="Hello world!")
      
        await self.close()
        await self.close(code=4123)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('chat_online',self.channel_name)
        print(close_code)
    
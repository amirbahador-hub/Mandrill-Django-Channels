from channels.generic.websocket import AsyncWebsocketConsumer
import json


class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("email", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("email", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        return await super().receive(text_data, bytes_data)

    async def add_event(self, arg):
        event = arg['event']
        await self.send(json.dumps(event))
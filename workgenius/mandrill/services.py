from django.core.cache import cache
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()

def update_socket(event:dict):
    async_to_sync(channel_layer.group_send)('email', {'type': 'add_event', 'event': event})

def create_event(event:dict):
    """
        Store Events in Redis
    """
    cache.set(event["_id"],event["msg"])

def store_message_payload(events:list):
    for event in events:
        create_event(event)
        update_socket(event)
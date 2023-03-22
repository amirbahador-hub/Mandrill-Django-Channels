from django.core.cache import cache
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .utils import EmailEvent


channel_layer = get_channel_layer()

def notify_event(event:dict):
    """
    call sockets
    """
    async_to_sync(channel_layer.group_send)('email', {'type': 'add_event', 'event': event})


def store_event(event:dict):
    """
        Store Events in Redis
    """
    cache.set(event["_id"],event["msg"])


def store_message_payload(events:list):
    for data in events:
        event = EmailEvent(data)
        event.actions.append(store_event)
        event.actions.append(notify_event)
        event.broadcast()
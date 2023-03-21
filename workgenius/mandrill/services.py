from django.core.cache import cache


def create_event(event:dict):
    """
        Store Events in Redis
    """
    cache.set(event["_id"],event["msg"])

def store_message_payload(events:list):
    #for p in events:
     #   create_event(p)
    responses = list(map(create_event, events))
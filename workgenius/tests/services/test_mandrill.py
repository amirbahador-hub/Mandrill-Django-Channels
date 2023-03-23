import pytest
from django.core.cache import cache
from workgenius.mandrill.services import store_event, store_message_payload


@pytest.mark.django_db
def test_store_event(event_serialized):
    event_id = event_serialized.get("_id")
    store_event(event_serialized)
    assert cache.get(event_id) == event_serialized.get("msg")
 

@pytest.mark.django_db
def test_store_payload(events_serialized):
    event_id = events_serialized[0].get("_id")
    store_message_payload(events_serialized)
    assert cache.get(event_id) == events_serialized[0].get("msg")
 

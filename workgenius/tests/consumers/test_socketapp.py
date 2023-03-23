import pytest
from channels.testing import WebsocketCommunicator
from workgenius.socketapp.consumer import EventConsumer

@pytest.mark.asyncio
async def test_my_consumer():
    communicator = WebsocketCommunicator(EventConsumer.as_asgi(), "GET", "ws/email/")
    connected, subprotocol = await communicator.connect()
    assert connected
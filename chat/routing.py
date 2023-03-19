from django.urls import re_path
from chat.consumers import ChatRoomConsumer

websocket_urlpatterns = [
    re_path("ws/chat/(?P<room_name>\w+)/$", ChatRoomConsumer)
]
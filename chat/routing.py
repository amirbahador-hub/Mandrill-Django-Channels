from django.urls import re_path
from chat.consumers import ChatRoomConsumer, ChatConsumer

websocket_urlpatterns = [
    #re_path("ws/chat/(?P<room_name>\w+)/$", ChatConsumer)
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatRoomConsumer.as_asgi()),

]
from django.urls import path
from .consumer import EventConsumer

ws_urlpatterns = [
    path('ws/email/', EventConsumer.as_asgi())
]
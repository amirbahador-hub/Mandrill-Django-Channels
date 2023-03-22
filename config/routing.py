import os
from .asgi import application as django_asgi_app
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from workgenius.socketapp.routing import ws_urlpatterns


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
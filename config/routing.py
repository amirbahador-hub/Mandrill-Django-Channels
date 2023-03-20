import os
from .asgi import application as django_asgi_app
from channels.routing import ProtocolTypeRouter


application = ProtocolTypeRouter({
    "http": django_asgi_app,
})
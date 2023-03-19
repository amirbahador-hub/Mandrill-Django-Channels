"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


#application = ProtocolTypeRouter(
#E    {
#        "http": get_asgi_application(),
#        # Just HTTP for now. (We can add other protocols later.)
#    }
#)

django_asgi_app = get_asgi_application()

application  = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
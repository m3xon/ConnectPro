"""
ASGI config for myPro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# your_project/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myPro.routing import websocket_urlpatterns  # Import the routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myPro.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)  # Attach the routing
    ),
})




import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import backend.chat.routing as chat


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_settings.settings')

application = ProtocolTypeRouter({
    'https': get_asgi_application(),
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.websocket_urlpartterns
        )
    )
})


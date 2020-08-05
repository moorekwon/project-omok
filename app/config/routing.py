from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from chat.consumers import ChatConsumer
from omok.consumers import OmokConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
                re_path(r'ws/omok/(?P<room_name>\w+)/$', OmokConsumer),
            ]
        )
    ),
})

ASGI_APPLICATION = "config.routing.application"

from django.urls import re_path

from . import consumers

websocket_urlpattenrs = [
    re_path(r'wss/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer)
]

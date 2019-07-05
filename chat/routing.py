from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    path('/chat/<room_name>/', ChatConsumer)
]

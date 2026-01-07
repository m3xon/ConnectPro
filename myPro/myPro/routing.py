from django.urls import path
from chatting_app import consumers  # Make sure this points to the correct app and consumer

websocket_urlpatterns = [
    path('ws/chat/<int:roomId>/', consumers.ChatConsumer.as_asgi()),  # P2P chat
]

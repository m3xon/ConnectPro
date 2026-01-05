from django.urls import path
from .views import on_chat

urlpatterns = [
    path("", on_chat, name= "chat" )
]
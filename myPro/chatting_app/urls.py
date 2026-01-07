from django.urls import path, re_path
from .views import on_chat, select_chat

urlpatterns = [
    re_path(r'^(?P<roomId>\d+)?/?$', on_chat, name="chat"),
    path("sel_chat/<int:curId>/", select_chat, name = "sel_chat"),
]
from django.urls import path
from .views import on_discover, connect
urlpatterns = [
    path('', on_discover, name = 'discover'),
    path('connect/<int:id>/', connect, name='connect'),
]
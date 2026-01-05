from django.urls import path
from .views import home, registAccount, loginAccount

urlpatterns = [
    path('', home, name = 'home'),
    path('register', registAccount, name = 'register'),
    path('login', loginAccount, name = 'login'),
]
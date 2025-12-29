from django.urls import path
from .views import home, registAccount, loginAccount, on_profile

urlpatterns = [
    path('', home, name = 'home'),
    path('register', registAccount, name = 'register'),
    path('login', loginAccount, name = 'login'),
    path('profile', on_profile, name = 'profile'),

]
from django.urls import path
from .views import on_profile, EditProfileView
urlpatterns = [
    path('', on_profile, name = 'profile'),
    path('edit_profile', EditProfileView.as_view(), name = 'edit_profile'),
]
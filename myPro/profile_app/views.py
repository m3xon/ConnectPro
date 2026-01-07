from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from connect_app.models import UserMd

def on_profile(request):
    userId = request.session.get('userId', 0)
    if userId:
        userInfo = UserMd.objects.get(id= userId)
        profileInfo = Profile.objects.get(user__id= userId)
        
        return render(request, 'profile/profile.html', {'userInfo': userInfo, 'profileInfo': profileInfo})
    return HttpResponse("No user information arrived!")


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/edit.html'
    success_url = '/profile'  # Redirect to profile page after saving
    def get_object(self, queryset=None):
        return self.request.user.profile  # Get the profile of the logged-in user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating your profile.")
        return super().form_invalid(form)


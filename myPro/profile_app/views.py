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
    
    # Define success URL to redirect after a successful form submission
    success_url = '/profile'  # Redirect to profile page after saving

    # This ensures the correct profile is updated (the currently logged-in user's profile)
    def get_object(self, queryset=None):
        return self.request.user.profile  # Get the profile of the logged-in user

    def form_valid(self, form):
        # Before saving, check if the fields that should be unique are unchanged
        # if form.cleaned_data.get('email') == self.request.user.profile.email:
        #     form.cleaned_data['email'] = self.request.user.profile.email  # Reset unchanged email field

        # Now, call the original form_valid to save the instance
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating your profile.")
        return super().form_invalid(form)


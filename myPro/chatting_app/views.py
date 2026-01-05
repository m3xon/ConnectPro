from django.shortcuts import render
from profile_app.models import Profile
# Create your views here.

def on_chat(request):
    userId = request.user.id
    profileInfo = Profile.objects.get(user__id = userId)
    return render(request, "chatting/chat.html", {'profileInfo': profileInfo})

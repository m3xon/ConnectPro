from django.shortcuts import render, redirect
from profile_app.models import Profile
from discover_app.models import Room
# Create your views here.

def on_chat(request, roomId = 0):
    userId = request.user.id
    profileInfo = Profile.objects.get(user__id = userId)
    return render(request, "chatting/chat.html", {'profileInfo': profileInfo, 'roomId': int(roomId)})

def select_chat(reuqest, curId):
    #Find the correct room
    userId = reuqest.user.id
    if reuqest.user.user_type == 'client':
        room = Room.objects.get(client__id = userId, developer__id = curId)
    else:
        room = Room.objects.get(developer__id = userId, client__id = curId)
    return redirect('chat', roomId= room.id)
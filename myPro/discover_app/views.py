from django.shortcuts import render, redirect
from profile_app.models import Profile
from django.core.paginator import Paginator
from connect_app.models import UserMd
from .models import Room

def on_discover(request):
    cur_user_type = request.user.user_type
    userId = request.user.id
    profileInfo = Profile.objects.get(user__id = userId)

    if cur_user_type == 'client':
        profiles = Profile.objects.filter(user__user_type='developer')
        friends = Room.objects.filter(client__id = userId).values_list('developer__id', flat= True)
        connections = Profile.objects.filter(user__id__in = friends)
    else:
        profiles = Profile.objects.filter(user__user_type='client') 
        friends = Room.objects.filter(developer__id = userId).values_list('client__id', flat= True)
        connections = Profile.objects.filter(user__id__in = friends)
    print(userId, "------------------------------", connections)
    paginator = Paginator(profiles, 3)  # Show 10 profiles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'discover/discover.html', {'page_obj': page_obj, 'profileInfo': profileInfo, 'connections': connections})

def connect(request, id):
    user = UserMd.objects.get(id = id)
    if request.user.user_type == 'client':
        print(Room.objects.create(client = request.user, developer = user))
    else:
        print(Room.objects.create(client = user, developer = request.user))

    return redirect("discover")
    

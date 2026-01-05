from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import LoginForm, RegistFrom
from django.db import IntegrityError
from django.template import Context
from .models import UserMd
from django.contrib.auth import authenticate, login
from django.contrib import messages
from profile_app.models import Profile
# Create your views here.

def home(request):
    return render(request, 'home.html')


def registAccount(request):
    if request.method == 'POST':
        form = RegistFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")            
            return redirect("login")
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistFrom()
    return render(request, 'register.html', {"form": form})


def loginAccount(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username = email, password = password)
            if user is not None:
                login(request, user)
                request.session['userId'] = user.id
                messages.success(request, "Login successful.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid email or password..")
                return render(request, "login.html", {'form': form})
        else:
            messages.error(request, "There was an error with your login. Please try again.")
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html',{"form": form})


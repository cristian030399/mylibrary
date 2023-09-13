from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User


def show_signup_form(request):
    return render(request, 'registration/signup.html')


def create_user(request):
    try:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        userExist = User.objects.filter(username=username).exists()
        if (userExist):
            return render(request, 'registration/signup.html', {
                "error_message": "User already exist.",
            })
        newUser = User.objects.create_user(username=username, email=email, password=password)
    except (KeyError):
        return render(request, 'registration/signup.html', {
            "error_message": "Complete all fields.",
        })
    else:        
        newUser.save()
        return HttpResponseRedirect(reverse('auth:login'))

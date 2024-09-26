from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import User


def signup(request):
    if request.user.is_authenticated:
        print('user authenticated')
        return redirect('/')

    return render(request, 'users/signup.html')


def login_user(request):
    return render(
        request,
        'users/login.html',
    )


def logout_user(request):
    logout(request)
    return redirect('/')

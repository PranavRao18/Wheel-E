from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def dashboard_view(request):
    return render(request, 'registration/dashboard.html')

def landing_view(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request,"about_us.html")
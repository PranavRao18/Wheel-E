from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accountConfig.models import User
from datetime import datetime, timedelta
import random

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'auth/login.html', status=401)
            
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')    

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cfmpassword = request.POST.get('Confirmpassword')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        username = email.split('@')[0]
        
        if password != cfmpassword:
            messages.info(request,'Password and Confirm Password doesnot match!')
            return redirect('register')
            
        try:
            user = User.objects.create_user(email=email, username=username, password=password)
        except:
            messages.error(request,'Error Creating Account Contact Support')
            return redirect('register')
        user.phone_number = phone
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        login(request,user)
        return redirect('dashboard')
    return render(request,'auth/signup.html')

def register_driver(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cfmpassword = request.POST.get('Confirmpassword')
        firstname = request.POST.get('firstname')
        dob = request.POST.get('dob')
        driverLicense = request.POST.get('license')
        phone = request.POST.get('phone')
        username = email.split('@')[0]
        print("hello")
        if password != cfmpassword:
            messages.info(request,'Password and Confirm Password doesnot match!')
            print(username)
            return redirect('driverreg')
            
        try:
            user = User.objects.create_user(email=email, username=username, password=password)
            print(username)
        except:
            messages.error(request,'Error Creating Account Contact Support')
            return redirect('driverreg')
        user.license_number = driverLicense
        user.date_of_birth = dob
        user.phone_number = phone
        user.first_name = firstname
        user.save()
        login(request,user)
        return redirect('driver_dashboard')
    return render(request,'auth/register_driver.html')
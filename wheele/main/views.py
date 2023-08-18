from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')  # Check if the "Remember Me" checkbox is selected
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                # Set session expiration to 0 if "Remember Me" is not selected (session will expire on browser close)
                request.session.set_expiry(0)
            return redirect('dashboard')
    return render(request, 'registration/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'registration/dashboard.html')

def landing_view(request):
    return render(request, 'home.html')
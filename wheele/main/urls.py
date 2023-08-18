from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('',views.landing_view,name = "home"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

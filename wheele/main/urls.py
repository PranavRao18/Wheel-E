from django.urls import path
from . import views
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('',views.landing_view,name = "home"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
]

from django.urls import path
from . import views
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('',views.landing_view,name = "home"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('aboutus',views.about_us,name='aboutus'),
    path('api',views.handle_request,name='api'),
    path('userprofile',views.user_profile,name = 'userprofile'),
    path('loading',views.load,name='load')
]

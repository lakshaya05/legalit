from django.urls import path,include
from django.contrib import admin
from .views import about_view, home_view, login_view, logout_view, register_view


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
]
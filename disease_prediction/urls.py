"""
Disease Prediction System - URLs
This file defines the URL patterns for the application.
Each URL pattern maps to a specific view function.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page URL
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Core functionality URLs
    path('predict/', views.predict_disease, name='predict'),
    
    # Information pages URLs
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 
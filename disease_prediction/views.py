"""
Disease Prediction System - Views
This file contains all the view functions for handling HTTP requests and responses.
Includes authentication, prediction, and recommendation views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from .models import (
    SymptomSeverity, DiseaseTraining, DiseaseDescription,
    DiseaseDiet, DiseaseMedicine, DiseasePrecaution, DiseaseWorkout,
    
)
from fuzzywuzzy import process
from django.views.decorators.csrf import csrf_protect
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def home(request):
    """
    Home page view.
    Renders the main landing page of the application.
    """
    return render(request, 'home.html')

def load_symptoms():
    """Load available symptoms from the database."""
    symptoms = SymptomSeverity.objects.values_list('symptom', flat=True)
    return {symptom.lower(): symptom for symptom in symptoms}

def predict_disease(patient_symptoms):
    """Predict disease based on input symptoms."""
    if not patient_symptoms:
        return "No symptoms provided", {}, {}

    # Query to find diseases with matching symptoms
    diseases = DiseaseTraining.objects.filter(
        symptom1__in=patient_symptoms
    ).values('disease').annotate(
        symptom_matches=Count('disease')
    ).order_by('-symptom_matches')[:1]

    if not diseases:
        return "Unknown Disease", {}, {}

    disease = diseases[0]['disease']
    disease_data = {}
    recommendations = {}

    # Get disease description
    try:
        description = DiseaseDescription.objects.get(disease=disease)
        disease_data['description'] = description.description
    except DiseaseDescription.DoesNotExist:
        disease_data['description'] = "No description available."

    # Get diet recommendations
    try:
        diet = DiseaseDiet.objects.get(disease=disease)
        recommendations['diet'] = [
            item for item in [diet.diet1, diet.diet2, diet.diet3, diet.diet4]
            if item and item.strip()
        ]
    except DiseaseDiet.DoesNotExist:
        recommendations['diet'] = ["No diet recommendations."]

    # Get medicine recommendations
    try:
        medicine = DiseaseMedicine.objects.get(disease=disease)
        recommendations['medicine'] = [
            item for item in [medicine.medicine1, medicine.medicine2, medicine.medicine3, medicine.medicine4]
            if item and item.strip()
        ]
    except DiseaseMedicine.DoesNotExist:
        recommendations['medicine'] = ["No medicine recommendations."]

    # Get precautions
    try:
        precaution = DiseasePrecaution.objects.get(disease=disease)
        recommendations['precautions'] = [
            item for item in [precaution.precaution1, precaution.precaution2, precaution.precaution3, precaution.precaution4]
            if item and item.strip()
        ]
    except DiseasePrecaution.DoesNotExist:
        recommendations['precautions'] = ["No precautions available."]

    # Get workout recommendations
    try:
        workout = DiseaseWorkout.objects.get(disease=disease)
        recommendations['workout'] = [
            item for item in [workout.workout1, workout.workout2, workout.workout3, workout.workout4]
            if item and item.strip()
        ]
    except DiseaseWorkout.DoesNotExist:
        recommendations['workout'] = ["No workout recommendations."]

    return disease, disease_data, recommendations

def signup(request):
    """
    User registration view.
    Handles new user registration and account creation.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate input
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'signup.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')

        try:
            # Create new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def login_view(request):
    """
    User login view.
    Handles user login and authentication.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # First try to get user by email
            user = User.objects.get(email=email)
            # Then authenticate with username and password
            authenticated_user = authenticate(request, username=user.username, password=password)
            
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('predict')
            else:
                messages.error(request, "Invalid password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email. Please sign up first.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@csrf_protect
def predict_view(request):
    """
    Disease prediction view.
    Handles symptom input and disease prediction using ML model.
    Returns prediction results and recommendations.
    """
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms', '').split(',')
        symptoms = [s.strip() for s in symptoms if s.strip()]
        
        predicted_disease, disease_data, recommendations = predict_disease(symptoms)
        
        return render(request, 'index.html', {
            'symptoms': ', '.join(symptoms),
            'predicted_disease': predicted_disease,
            'dis_des': disease_data.get('description', 'No description.'),
            'my_diet': recommendations.get('diet', []),
            'my_precautions': recommendations.get('precautions', []),
            'medications': recommendations.get('medicine', []),
            'workout': recommendations.get('workout', []),
            'prediction_source': "Symptom Analysis"
        })
    return render(request, 'index.html')

def about(request):
    """
    About page view.
    Displays information about the application and its features.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Contact page view.
    Provides contact information and support details.
    """
    return render(request, 'contact.html')

def view_users(request):
    """View to display all registered users."""
    if not request.user.is_superuser:
        messages.error(request, "Only administrators can view user list.")
        return redirect('home')
    
    users = User.objects.all().order_by('date_joined')
    return render(request, 'users.html', {'users': users}) 
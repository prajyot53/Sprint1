"""
Disease Prediction System - Admin
This file configures the Django admin interface.
Registers models and customizes their admin views.
"""

from django.contrib import admin
from .models import (
    SymptomSeverity,
    DiseaseTraining,
    DiseaseDescription,
    DiseaseDiet,
    DiseaseMedicine,
    DiseasePrecaution,
    DiseaseWorkout
)

@admin.register(SymptomSeverity)
class SymptomSeverityAdmin(admin.ModelAdmin):
    """
    Admin configuration for SymptomSeverity model.
    Customizes how symptoms and their severity weights are displayed in admin.
    """
    list_display = ('symptom', 'weight')
    search_fields = ('symptom',)
    ordering = ('-weight',)

@admin.register(DiseaseTraining)
class DiseaseTrainingAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseaseTraining model.
    Manages disease training data in admin interface.
    """
    list_display = ('disease', 'symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5')
    search_fields = ('disease', 'symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5')
    list_filter = ('disease',)

@admin.register(DiseaseDescription)
class DiseaseDescriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseaseDescription model.
    Handles disease descriptions in admin interface.
    """
    list_display = ('disease', 'description')
    search_fields = ('disease',)

@admin.register(DiseaseDiet)
class DiseaseDietAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseaseDiet model.
    Manages dietary recommendations in admin interface.
    """
    list_display = ('disease', 'diet1', 'diet2', 'diet3', 'diet4')
    search_fields = ('disease',)

@admin.register(DiseaseMedicine)
class DiseaseMedicineAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseaseMedicine model.
    Handles medicine recommendations in admin interface.
    """
    list_display = ('disease', 'medicine1', 'medicine2', 'medicine3', 'medicine4')
    search_fields = ('disease',)

@admin.register(DiseasePrecaution)
class DiseasePrecautionAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseasePrecaution model.
    Manages precautionary measures in admin interface.
    """
    list_display = ('disease', 'precaution1', 'precaution2', 'precaution3', 'precaution4')
    search_fields = ('disease',)

@admin.register(DiseaseWorkout)
class DiseaseWorkoutAdmin(admin.ModelAdmin):
    """
    Admin configuration for DiseaseWorkout model.
    Handles workout recommendations in admin interface.
    """
    list_display = ('disease', 'workout1', 'workout2', 'workout3', 'workout4')
    search_fields = ('disease',) 
"""
Disease Prediction System - Models
This file contains all the database models for the Disease Prediction System.
Each model represents a table in the PostgreSQL database.
"""

from django.db import models
from django.contrib.auth.models import User

class SymptomSeverity(models.Model):
    """
    Model to store symptom severity weights.
    Used for calculating disease probability based on symptom importance.
    """
    symptom = models.CharField(max_length=100, unique=True, verbose_name="Symptom Name")
    weight = models.IntegerField()

    class Meta:
        db_table = 'symptom_severity_data'

    def __str__(self):
        return f"{self.symptom} (Weight: {self.weight})"

class DiseaseTraining(models.Model):
    """
    Model to store training data for disease prediction.
    Contains disease names and their associated symptoms.
    Used by the ML model for training and prediction.
    """
    disease = models.CharField(max_length=100)
    symptom1 = models.CharField(max_length=100, null=True, blank=True)
    symptom2 = models.CharField(max_length=100, null=True, blank=True)
    symptom3 = models.CharField(max_length=100, null=True, blank=True)
    symptom4 = models.CharField(max_length=100, null=True, blank=True)
    symptom5 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'disease_training_data'

    def __str__(self):
        return self.disease

class DiseaseDescription(models.Model):
    """
    Model to store detailed descriptions of diseases.
    Provides comprehensive information about each disease.
    """
    disease = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'disease_description'

    def __str__(self):
        return self.disease

class DiseaseDiet(models.Model):
    """
    Model to store dietary recommendations for diseases.
    Contains specific diet plans for different diseases.
    """
    disease = models.CharField(max_length=100, unique=True)
    diet1 = models.CharField(max_length=200, null=True, blank=True)
    diet2 = models.CharField(max_length=200, null=True, blank=True)
    diet3 = models.CharField(max_length=200, null=True, blank=True)
    diet4 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'disease_diet'

    def __str__(self):
        return f"Diet for {self.disease}"

class DiseaseMedicine(models.Model):
    """
    Model to store medicine recommendations for diseases.
    Contains prescribed medications for different diseases.
    """
    disease = models.CharField(max_length=100, unique=True)
    medicine1 = models.CharField(max_length=200, null=True, blank=True)
    medicine2 = models.CharField(max_length=200, null=True, blank=True)
    medicine3 = models.CharField(max_length=200, null=True, blank=True)
    medicine4 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'disease_medicine'

    def __str__(self):
        return f"Medicine for {self.disease}"

class DiseasePrecaution(models.Model):
    """
    Model to store precautionary measures for diseases.
    Contains preventive steps and safety measures.
    """
    disease = models.CharField(max_length=100, unique=True)
    precaution1 = models.CharField(max_length=200, null=True, blank=True)
    precaution2 = models.CharField(max_length=200, null=True, blank=True)
    precaution3 = models.CharField(max_length=200, null=True, blank=True)
    precaution4 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'disease_precaution'

    def __str__(self):
        return f"Precautions for {self.disease}"

class DiseaseWorkout(models.Model):
    """
    Model to store workout/exercise recommendations for diseases.
    Contains physical activity suggestions for different diseases.
    """
    disease = models.CharField(max_length=100, unique=True)
    workout1 = models.CharField(max_length=200, null=True, blank=True)
    workout2 = models.CharField(max_length=200, null=True, blank=True)
    workout3 = models.CharField(max_length=200, null=True, blank=True)
    workout4 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'disease_workout'

    def __str__(self):
        return f"Workout for {self.disease}" 
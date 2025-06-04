from django.core.management.base import BaseCommand
from disease_prediction.models import SymptomSeverity, DiseaseTraining

class Command(BaseCommand):
    help = 'Add symptoms to the database'

    def handle(self, *args, **kwargs):
        # List of symptoms with their severity weights
        symptoms = [
            ('fever', 4),
            ('high_fever', 5),
            ('low_fever', 3),
            ('chills', 3),
            ('sweating', 2),
            ('body_ache', 3),
            ('headache', 3),
            ('fatigue', 2),
            ('cough', 3),
            ('sore_throat', 3),
            ('runny_nose', 2),
            ('congestion', 2),
            ('sneezing', 2),
            ('shortness_of_breath', 5),
            ('chest_pain', 5),
            ('nausea', 3),
            ('vomiting', 4),
            ('diarrhea', 4),
            ('abdominal_pain', 4),
            ('loss_of_appetite', 2),
            ('muscle_pain', 3),
            ('joint_pain', 3),
            ('rash', 3),
            ('itching', 2),
            ('swelling', 3),
            ('dizziness', 3),
            ('confusion', 4),
            ('seizures', 5),
            ('loss_of_taste', 3),
            ('loss_of_smell', 3)
        ]

        # Add symptoms to SymptomSeverity table
        for symptom, weight in symptoms:
            SymptomSeverity.objects.get_or_create(
                symptom=symptom,
                defaults={'weight': weight}
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added symptom: {symptom}'))

        # Add some common disease-symptom combinations
        disease_symptoms = [
            ('Common Cold', ['fever', 'cough', 'sore_throat', 'runny_nose', 'congestion']),
            ('Flu', ['high_fever', 'chills', 'body_ache', 'fatigue', 'cough']),
            ('COVID-19', ['fever', 'cough', 'shortness_of_breath', 'loss_of_taste', 'loss_of_smell']),
            ('Pneumonia', ['high_fever', 'cough', 'shortness_of_breath', 'chest_pain', 'fatigue']),
            ('Gastroenteritis', ['fever', 'nausea', 'vomiting', 'diarrhea', 'abdominal_pain']),
            ('Dengue', ['high_fever', 'severe_headache', 'body_ache', 'rash', 'fatigue']),
            ('Malaria', ['high_fever', 'chills', 'sweating', 'body_ache', 'fatigue']),
            ('Typhoid', ['high_fever', 'headache', 'abdominal_pain', 'loss_of_appetite', 'fatigue']),
            ('Chickenpox', ['fever', 'rash', 'itching', 'body_ache', 'fatigue']),
            ('Measles', ['high_fever', 'cough', 'runny_nose', 'rash', 'conjunctivitis'])
        ]

        # Add disease-symptom combinations to DiseaseTraining table
        for disease, symptom_list in disease_symptoms:
            DiseaseTraining.objects.get_or_create(
                disease=disease,
                defaults={
                    'symptom1': symptom_list[0] if len(symptom_list) > 0 else None,
                    'symptom2': symptom_list[1] if len(symptom_list) > 1 else None,
                    'symptom3': symptom_list[2] if len(symptom_list) > 2 else None,
                    'symptom4': symptom_list[3] if len(symptom_list) > 3 else None,
                    'symptom5': symptom_list[4] if len(symptom_list) > 4 else None
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added disease: {disease}')) 
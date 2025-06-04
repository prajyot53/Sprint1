# Disease Prediction and Medical Recommendation System

A Django-based web application that predicts diseases based on symptoms and provides medical recommendations.

## Features

- Disease prediction based on symptoms
- User authentication system
- Medical recommendations including:
  - Diet recommendations
  - Medicine suggestions
  - Precautions
  - Workout recommendations
- Detailed disease descriptions

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the database:
- Make sure MySQL is installed and running
- Create a database named 'healthcare_system'
- Update database credentials in `healthcare_project/settings.py` if needed

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application at: http://localhost:8000

## Usage

1. Sign up for a new account or log in with existing credentials
2. Navigate to the prediction page
3. Enter symptoms (comma-separated)
4. Get disease prediction and recommendations

## Project Structure

- `disease_prediction/` - Main Django app
  - `models.py` - Database models
  - `views.py` - View functions
  - `templates/` - HTML templates
- `healthcare_project/` - Django project settings
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates

## Technologies Used

- Django 5.0.2
- MySQL
- Python 3.x
- FuzzyWuzzy for string matching 
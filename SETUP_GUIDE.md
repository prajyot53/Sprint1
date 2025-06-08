# Disease Prediction System - Setup Guide

## Prerequisites
Before running the project, ensure you have the following installed:

### 1. Python Installation
- Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Verify installation by running in command prompt:
  ```bash
  python --version
  ```

### 2. PostgreSQL Installation
- Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/)
- During installation:
  - Remember the password you set for the postgres user
  - Keep the default port (5432)
  - Complete the installation
- Verify installation by running:
  ```bash
  psql --version
  ```

### 3. Git Installation (Optional)
- Download and install Git from [git-scm.com](https://git-scm.com/downloads)
- Verify installation:
  ```bash
  git --version
  ```

## Project Setup

### 1. Extract the Project
- Extract the zip file to your desired location
- Open command prompt/terminal in the project directory

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Open PostgreSQL
2. Create a new database:
   ```sql
   CREATE DATABASE disease_prediction;
   ```
3. Update database settings in `healthcare_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'disease_prediction',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
- Follow prompts to create admin account

### 7. Load Initial Data
```bash
python manage.py loaddata initial_data.json
```

### 8. Run Development Server
```bash
python manage.py runserver
```

## Accessing the Application
1. Open web browser
2. Go to: `http://127.0.0.1:8000/`
3. For admin panel: `http://127.0.0.1:8000/admin/`

## Troubleshooting

### Common Issues

1. **Python not found**
   - Ensure Python is added to PATH
   - Restart command prompt

2. **PostgreSQL connection error**
   - Verify PostgreSQL service is running
   - Check database credentials in settings.py
   - Ensure database exists

3. **Module not found**
   - Activate virtual environment
   - Run `pip install -r requirements.txt` again

4. **Migration errors**
   - Delete migration files in migrations folder (except __init__.py)
   - Run `python manage.py makemigrations` again
   - Then run `python manage.py migrate`

### Required Python Packages
The following packages will be installed via requirements.txt:
- Django
- psycopg2-binary
- scikit-learn
- pandas
- numpy
- pillow
- django-crispy-forms
- crispy-bootstrap4

## Additional Notes
1. Keep the virtual environment activated while working on the project
2. Never commit the virtual environment folder
3. Keep your database credentials secure
4. Regular backups of the database are recommended

## Support
If you encounter any issues:
1. Check the error messages in the console
2. Verify all prerequisites are installed correctly
3. Ensure all steps in the setup guide are followed
4. Contact the project maintainer for assistance 
"""
WSGI config for healthcare_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_project.settings')

application = get_wsgi_application() 
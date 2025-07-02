"""
Django settings for mashinani project.
Updated for Netlify frontend integration
"""

from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url  # Added for better database configuration

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'fe)up@wkbf+)_7g@1bwo)2o!tzckg^hwhyk0_ugn$ncdf8+8=k')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts - remove protocol and trailing slashes
ALLOWED_HOSTS = [
    'mashinani-2.onrender.com',
    'job-portal-davidwachira.netlify.app',
    'localhost',
    '127.0.0.1'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'drf_spectacular',
    'rest_framework',
    'django_filters',
]

# Database configuration - using dj-database-url for reliability
DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL', 
        'postgresql://mashinani_db_user:brUwuY8QYnyts7S6bziiWnPCNMxt7Yuj@dpg-d1h9v57fte5s739gsmug-a.oregon-postgres.render.com:5432/mashinani_db')
    )
}

# CORS and Security Settings
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'https://job-portal-davidwachira.netlify.app',
    'http://localhost:3000',
    'http://localhost:5173',
]

CSRF_TRUSTED_ORIGINS = [
    'https://mashinani-2.onrender.com',
    'https://job-portal-davidwachira.netlify.app',
]

# Cookie settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
CORS_ALLOW_CREDENTIALS = True

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_COOKIE': 'access_token',
    'AUTH_COOKIE_SECURE': True,
    'AUTH_COOKIE_SAMESITE': 'None',
}

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Core settings
ROOT_URLCONF = 'mashinani.urls'
AUTH_USER_MODEL = 'core.User'
WSGI_APPLICATION = 'mashinani.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
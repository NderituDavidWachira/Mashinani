"""
Django settings for mashinani project.
Updated for Netlify frontend integration
"""

from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'fe)up@wkbf+)_7g@1bwo)2o!tzckg^hwhyk0_ugn$ncdf8+8=k')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts - add your Render and Netlify URLs
ALLOWED_HOSTS = [
    'https://mashinani-2.onrender.com/',  # Render backend URL
    'https://job-portal-davidwachira.netlify.app',  # Netlify frontend URL
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

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CORS and Security Settings for Netlify
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'https://job-portal-davidwachira.netlify.app',  # Netlify frontend
    'http://localhost:3000',                 # Local development
    'http://localhost:5173',                 # Vite development
]
CSRF_TRUSTED_ORIGINS = [
    'https://mashinani-2.onrender.com/',  # Render backend
    'https://job-portal-davidwachira.netlify.app',  # Netlify frontend
]

# Cookie settings for cross-site requests
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
        'rest_framework.permissions.IsAuthenticated',
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

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Other settings remain the same...
ROOT_URLCONF = 'mashinani.urls'
AUTH_USER_MODEL = 'core.User'
WSGI_APPLICATION = 'mashinani.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
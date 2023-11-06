"""
Django settings for app_settings project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gvdgiwq3br$xn(bb1yb*2yzdra&_k&6+9($3gx+j0+s44a@*e6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', ]


# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'backend.authentication.apps.AuthenticationConfig',
    'backend.chat.apps.ChatConfig',
    'backend.user.apps.UserConfig',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "frontend/")],
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

#WSGI_APPLICATION = 'app_settings.wsgi.application'
ASGI_APPLICATION = 'app_settings.asgi.application'
CHANNEL_LAYERS = {
    'default':{
        'BACKEND':'channels.layers.InMemoryChannelLayer',
    }
}


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "backend" / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(BASE_DIR, "cdn/", "static_cdn/")
MEDIA_ROOT = os.path.join(BASE_DIR, "cdn/", "media_cdn/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "frontend/" "assets/"),
    os.path.join(BASE_DIR, "frontend/" "assets/" "media/"),
)
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


##########################
##########################
## my custome settings ###
##########################
##########################

AUTH_USER_MODEL = "authentication.CustomUser"

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'some_random_text')
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'some_random_text')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
    EMAIL_PORT = os.environ.get('EMAIL_PORT', 'some_random_text')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'some_random_text') #sender's email-id
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'some_random_text')
    SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'some_random_text')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'some_random_text') #password associated with above email-id

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    #'backend.user.authentication.CustomModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_PREMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

REST_AUTH = {

    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY':True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': "refresh",
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ["BEARER"],
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=40),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(hours=72),
}

#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True

#ACCOUNT_FORMS = {'signup': 'backend.user.forms.RegistrationForm'}
#ACCOUNT_USERNAME_MIN_LENGTH = 10

ACCOUNT_EMAIL_REQUIRED = True

# REST_AUTH_REGISTER_SERIALIZERS ={
#     'REGISTER_SERIALIZER': 'user.serializers.RegisterSerializer'
# }

# REST_AUTH_SERIALIZERS ={
#     "LOGIN_SERIALIZER": 'user.serializers.LoginSerializer'
# }

###############
###############
#####
##### DJANGO CORES HEADER CONFIGURATION
#####
###############
###############
CORS_URLS_REGEX = r"^/api/.*$"

CORS_ALLOWED_ORIGINS = ["http://localhost:8000", "http://localhost:5500"]

if DEBUG:
    CORS_ALLOWED_ORIGINS += [
    "http://localhost:5500",
    "http://localhost:5500",
    ]

#APPEND_SLASH=False

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "Content-Type",
    "Authorization",
]
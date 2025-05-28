from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')

from base import *

# SECURITY WARNING: don't run with debug turned on in production!


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-test',
        'USER': 'django-test',
        'PASSWORD': 'django-test',
        'HOST': '10.20.30.203',
        'PORT': '3306',
    }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

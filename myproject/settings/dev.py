from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')

from base import *

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
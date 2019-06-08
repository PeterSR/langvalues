import os

from .base import * # Import base settings

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DATABASE"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "3306"),
    }
}

# In production SECRET KEY is read from a file

SECRET_KEY_FILE = os.getenv('SECRET_KEY_FILE', None)

# By default the key is located in the root of the Django app
if not SECRET_KEY_FILE:
    SECRET_KEY_FILE = os.path.join(BASE_DIR, "secret_key.txt")


with open(SECRET_KEY_FILE) as f:
    SECRET_KEY = f.read().strip()


DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, "build/static")

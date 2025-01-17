from .base import *

DEBUG = True
SECRET_KEY = 'keep-it-secret-keep-it-safe'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': VENV_DIR / 'db.sqlite3',
    }
}
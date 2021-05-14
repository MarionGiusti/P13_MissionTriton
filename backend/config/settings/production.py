from .defaults import *

DEBUG = False

ALLOWED_HOSTS = ['206.189.7.202']
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PWD'),
        'HOST': '',
        'PORT': '5432',
    }
}

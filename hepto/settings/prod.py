from .base import *




ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hepto',
        'USER': 'heptodba',
        'PASSWORD': os.getenv("DATABASE"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))a)f_b#(lo_v@cov$o)g*r8a$7%#51+*)&ybpy3!qz-8e__e1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'migiwara',
        'NAME': 'postgresql-cubic-41504',
    }
}

INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)

STATIC_ROOT = BASE_DIR
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# ALLOWED_HOSTS = ['react-django.herokuapp.com', '127.0.0.1:8000']
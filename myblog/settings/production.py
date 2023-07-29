import environ
import os
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

DATABASES = {
    'default': env.db(),
}


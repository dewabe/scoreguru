from .base import *

DEBUG = env('DEBUG', default=False)
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])
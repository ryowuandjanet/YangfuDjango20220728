import dj_database_url
import django_on_heroku
from decouple import config
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
  'ryowu-basic-blog.herokuapp.com',
  'ryowu.blog'
]

DATABASES = {'default': dj_database_url.config(default='sqlite://db.sqlite3',conn_max_age=600,ssl_require=False)}

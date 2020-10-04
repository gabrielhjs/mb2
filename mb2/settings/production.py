from .common import *
import django_heroku


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv('DEBUG') == True
ALLOWED_HOSTS = ["https://mariabenedita.herokuapp.com"]

django_heroku.settings(locals())

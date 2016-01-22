from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
STATIC_PATH = os.path.join(BASE_DIR, "static")
STATIC_URL = 'http://ahmrudi.github.io/assets/'
STATIC_ROOT = '/home/ahm_rudi/Desktop/ahmrudi/ahmrudi.github.io/assets'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
	os.path.join(os.path.dirname(__file__), "static"),
]

WSGI_APPLICATION = 'superposts.publish_wsgi.application'
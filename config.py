"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')

STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

TESTING = True
DEBUG = True # Turns on debugging features in Flask
EMAIL = "mohamedsaadmoustafa+colors@gmail.com" # For use in application emails
"""Flask configuration."""
FLASK_ENV = 'development'
SECRET_KEY = 'GDtfDCFYjD'

STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

TESTING = True
DEBUG = True # Turns on debugging features in Flask
EMAIL = "mohamedsaadmoustafa+colors@gmail.com" # For use in application emails

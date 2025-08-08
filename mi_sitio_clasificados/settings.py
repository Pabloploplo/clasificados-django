import os

# Railway configuration
if os.environ.get('RAILWAY_ENVIRONMENT'):
    DEBUG = False
    ALLOWED_HOSTS = ['*.railway.app', '127.0.0.1', 'localhost']
    # ... resto del código
    
    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-123')
    
    # Database
    import dj_database_url
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        DATABASES = {
            'default': dj_database_url.parse(database_url)
        }
    
    # Static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
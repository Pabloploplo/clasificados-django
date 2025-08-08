import os

# Railway configuration
if os.environ.get('RAILWAY_ENVIRONMENT'):
    DEBUG = False
    ALLOWED_HOSTS = ['*.railway.app', '127.0.0.1', 'localhost']
    
    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-123')
    
    # Database
    import dj_database_url
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        DATABASES = {
            'default': dj_database_url.parse(database_url)
        }
    else:
        # Fallback para desarrollo
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    
    # Static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
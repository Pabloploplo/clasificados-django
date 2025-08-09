web: python manage.py migrate && python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_sitio_clasificados.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    print('Superusuario creado')
" && python manage.py runserver 0.0.0.0:$PORT
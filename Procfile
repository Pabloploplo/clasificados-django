web: python manage.py migrate && python manage.py shell -c "from django.contrib.auth 
import get_user_model; User = get_user_model(); 
User.objects.filter(username='admin').delete(); 
User.objects.create_superuser('admin', 'admin@admin.com', 'admin123'); 
print('Superusuario admin creado')" && python manage.py runserver 0.0.0.0:$PORT
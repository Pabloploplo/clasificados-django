web: python manage.py migrate && echo "from django.contrib.auth import 
get_user_model; User = get_user_model(); 
User.objects.filter(username='admin').exists() or 
User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')" | python
manage.py shell && python manage.py runserver 0.0.0.0:$PORT
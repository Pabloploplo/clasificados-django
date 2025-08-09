from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crear superusuario automáticamente'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superusuario "admin" creado exitosamente'))
        else:
            self.stdout.write('Superusuario "admin" ya existe')
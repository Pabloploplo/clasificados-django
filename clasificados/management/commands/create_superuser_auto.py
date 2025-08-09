from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crear superusuario automáticamente'

    def handle(self, *args, **options):
        print("=== INICIANDO CREACION DE SUPERUSUARIO ===")
        User = get_user_model()
        
        # Eliminar usuario existente para asegurar que se cree nuevo
        User.objects.filter(username='admin').delete()
        print("Usuario admin eliminado si existía")
        
        # Crear nuevo superusuario
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        print(f"Superusuario creado: {user.username}")
        print("Email: admin@admin.com")
        print("Password: admin123")
        print("=== SUPERUSUARIO CREADO EXITOSAMENTE ===")
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, blank=True, help_text="Nombre del ícono (ej: car, home, phone)")
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
    def total_anuncios(self):
        return self.anuncios.filter(activo=True).count()

class Anuncio(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('reacondicionado', 'Reacondicionado'),
    ]
    
    TIPO_CHOICES = [
        ('venta', 'Venta'),
        ('compra', 'Compra'),
        ('alquiler', 'Alquiler'),
        ('intercambio', 'Intercambio'),
        ('servicio', 'Servicio'),
    ]
    
    # Información básica
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_negociable = models.BooleanField(default=False)
    
    # Categorización
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='anuncios')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='venta')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='usado')
    
    # Información del usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')
    nombre_contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email_contacto = models.EmailField(blank=True)
    
    # Ubicación
    ciudad = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    
    # Imagen principal
    imagen = models.ImageField(upload_to='anuncios/', blank=True, null=True)
    
    # Control del anuncio
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_expiracion = models.DateTimeField(null=True, blank=True)
    vistas = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalle_anuncio', kwargs={'pk': self.pk})
    
    def esta_vigente(self):
        if self.fecha_expiracion:
            return timezone.now() <= self.fecha_expiracion
        return True
    
    def incrementar_vistas(self):
        self.vistas += 1
        self.save(update_fields=['vistas'])
    
    def precio_display(self):
        if self.precio:
            precio_str = f"${self.precio:,.0f}"
            if self.precio_negociable:
                precio_str += " (Negociable)"
            return precio_str
        return "Consultar precio"

class ImagenAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen = models.ImageField(upload_to='anuncios/adicionales/')
    descripcion = models.CharField(max_length=200, blank=True)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Imagen Adicional"
        verbose_name_plural = "Imágenes Adicionales"
        ordering = ['orden']
    
    def __str__(self):
        return f"Imagen de {self.anuncio.titulo}"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='favoritos')
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('usuario', 'anuncio')
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        ordering = ['-fecha_agregado']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.anuncio.titulo}"
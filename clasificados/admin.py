from django.contrib import admin
from .models import Categoria, Anuncio, ImagenAnuncio, Favorito

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'total_anuncios', 'activa', 'fecha_creacion')
    list_filter = ('activa', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('activa',)
    prepopulated_fields = {'descripcion': ('nombre',)}

class ImagenAnuncioInline(admin.TabularInline):
    model = ImagenAnuncio
    extra = 3
    fields = ('imagen', 'descripcion', 'orden')

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 'categoria', 'tipo', 'precio_display', 
        'usuario', 'ciudad', 'activo', 'destacado', 
        'vistas', 'fecha_creacion'
    )
    list_filter = (
        'categoria', 'tipo', 'estado', 'activo', 
        'destacado', 'fecha_creacion', 'ciudad'
    )
    search_fields = ('titulo', 'descripcion', 'usuario__username', 'ciudad')
    list_editable = ('activo', 'destacado')
    readonly_fields = ('vistas', 'fecha_creacion', 'fecha_actualizacion')
    date_hierarchy = 'fecha_creacion'
    
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'descripcion', 'categoria', 'tipo', 'estado')
        }),
        ('Precio', {
            'fields': ('precio', 'precio_negociable')
        }),
        ('Contacto', {
            'fields': ('usuario', 'nombre_contacto', 'telefono', 'email_contacto')
        }),
        ('Ubicación', {
            'fields': ('ciudad', 'direccion')
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Control', {
            'fields': ('activo', 'destacado', 'fecha_expiracion')
        }),
        ('Estadísticas', {
            'fields': ('vistas', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ImagenAnuncioInline]
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo anuncio
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

@admin.register(ImagenAnuncio)
class ImagenAnuncioAdmin(admin.ModelAdmin):
    list_display = ('anuncio', 'descripcion', 'orden')
    list_filter = ('anuncio__categoria',)
    search_fields = ('anuncio__titulo', 'descripcion')

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'anuncio', 'fecha_agregado')
    list_filter = ('fecha_agregado', 'anuncio__categoria')
    search_fields = ('usuario__username', 'anuncio__titulo')
    date_hierarchy = 'fecha_agregado'
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Anuncios
    path('anuncio/<int:pk>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    path('mis-anuncios/', views.mis_anuncios, name='mis_anuncios'),
    path('editar/<int:pk>/', views.editar_anuncio, name='editar_anuncio'),
    path('eliminar/<int:pk>/', views.eliminar_anuncio, name='eliminar_anuncio'),
    
    # Favoritos
    path('favorito/<int:pk>/', views.toggle_favorito, name='toggle_favorito'),
    path('favoritos/', views.mis_favoritos, name='mis_favoritos'),
    
    # Categorías
    path('categoria/<int:pk>/', views.categoria_detalle, name='categoria_detalle'),
]
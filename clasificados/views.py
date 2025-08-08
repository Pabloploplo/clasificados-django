from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from .models import Anuncio, Categoria, Favorito
from .forms import AnuncioForm, BusquedaForm

# Formularios básicos por ahora
class AnuncioForm:
    pass

class BusquedaForm:
    pass

def home(request):
    """Vista principal con listado de anuncios"""
    # Obtener parámetros de búsqueda
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    # Filtrar anuncios activos
    anuncios = Anuncio.objects.filter(activo=True).select_related('categoria', 'usuario')
    
    # Aplicar filtros de búsqueda
    if query:
        anuncios = anuncios.filter(
            Q(titulo__icontains=query) | 
            Q(descripcion__icontains=query)
        )
    
    if categoria_id:
        anuncios = anuncios.filter(categoria_id=categoria_id)
    
    # Ordenar por destacados primero, luego por fecha
    anuncios = anuncios.order_by('-destacado', '-fecha_creacion')
    
    # Paginación
    paginator = Paginator(anuncios, 12)  # 12 anuncios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Datos para la vista
    categorias = Categoria.objects.filter(activa=True)
    
    context = {
        'page_obj': page_obj,
        'categorias': categorias,
        'query': query,
        'total_anuncios': paginator.count,
    }
    
    return render(request, 'clasificados/home.html', context)

def detalle_anuncio(request, pk):
    """Vista de detalle de un anuncio"""
    anuncio = get_object_or_404(Anuncio, pk=pk, activo=True)
    
    # Incrementar contador de vistas
    anuncio.incrementar_vistas()
    
    # Anuncios relacionados (misma categoría, excluyendo el actual)
    anuncios_relacionados = Anuncio.objects.filter(
        categoria=anuncio.categoria,
        activo=True
    ).exclude(pk=anuncio.pk)[:4]
    
    context = {
        'anuncio': anuncio,
        'anuncios_relacionados': anuncios_relacionados,
    }
    
    return render(request, 'clasificados/detalle.html', context)

@login_required
def crear_anuncio(request):
    """Vista para crear un nuevo anuncio"""
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
            messages.success(request, '¡Anuncio creado exitosamente!')
            return redirect('detalle_anuncio', pk=anuncio.pk)
    else:
        form = AnuncioForm()
    
    return render(request, 'clasificados/crear_anuncio.html', {'form': form})

def mis_anuncios(request):
    """Vista temporal para mis anuncios"""
    return HttpResponse("Mis anuncios - próximamente")

def editar_anuncio(request, pk):
    """Vista temporal para editar anuncio"""
    return HttpResponse("Editar anuncio - próximamente")

def eliminar_anuncio(request, pk):
    """Vista temporal para eliminar anuncio"""
    return HttpResponse("Eliminar anuncio - próximamente")

def toggle_favorito(request, pk):
    """Vista temporal para favoritos"""
    return JsonResponse({'error': 'Próximamente'})

def mis_favoritos(request):
    """Vista temporal para favoritos"""
    return HttpResponse("Favoritos - próximamente")

def categoria_detalle(request, pk):
    """Vista para mostrar anuncios de una categoría específica"""
    categoria = get_object_or_404(Categoria, pk=pk, activa=True)
    anuncios = Anuncio.objects.filter(
        categoria=categoria, 
        activo=True
    ).order_by('-destacado', '-fecha_creacion')
    
    # Paginación
    paginator = Paginator(anuncios, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categoria': categoria,
        'page_obj': page_obj,
        'total_anuncios': paginator.count,
    }
    
    return render(request, 'clasificados/categoria.html', context)
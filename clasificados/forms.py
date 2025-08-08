from django import forms
from .models import Anuncio, Categoria

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = [
            'titulo', 'descripcion', 'categoria', 'tipo', 'estado',
            'precio', 'precio_negociable', 'nombre_contacto', 
            'telefono', 'email_contacto', 'ciudad', 'direccion', 'imagen'
        ]
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_negociable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email_contacto': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

class BusquedaForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)
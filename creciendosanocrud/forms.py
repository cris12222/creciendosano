from django import forms
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import ProtectedError

from . import models

class MetaForm(forms.ModelForm):
    class Meta:
        model=models.MetaModelo
        fields=['nombre','objetivo','valor',
                'tema_central','tema_semanal',
                'periodo',
                'responsable','descripcion']
    
class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields=['nombre','subtema'] 
      
class EventoForm(forms.ModelForm):
    class Meta:
        model = models.Evento
        fields=['nombre','tipo','fecha','material',
                'cant_hombres','cant_mujeres','tema_central',
                'subtema','responsable','tiempo','meta',
                'descripcion','unidad_medida','area']

class FechaForm(forms.ModelForm):
    class Meta:
        model = models.getFecha
        fields=['fecha_inicio','fecha_fin']
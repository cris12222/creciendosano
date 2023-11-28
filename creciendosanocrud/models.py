from django.db import models
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel

#from users.models import AbstractFields

class MetaModelo( SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    tema_central = models.CharField(max_length=255)
    tema_semanal = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    class Meta:
        db_table = 'metas'
        ordering = ['-id']
    def __str__(self):
        return self.nombre

class Tema( SafeDeleteModel,models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    subtema = models.CharField(max_length=255)
    class Meta:
        db_table = 'temas'
        ordering = ['id']
    def __str__(self):
        return self.nombre
  
class Evento( SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    material = models.CharField(max_length=255)
    cant_hombres = models.IntegerField()
    cant_mujeres = models.IntegerField()
    tema_central = models.CharField(max_length=255)
    subtema = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    tiempo = models.CharField(max_length=255)
    meta = models.ForeignKey('MetaModelo',on_delete=models.DO_NOTHING,null=True)   
    unidad_medida = models.CharField(max_length=255)
    area = models.CharField(max_length=255) 
    descripcion = models.CharField(max_length=255)
    class Meta:
        db_table = 'eventos'
        ordering = ['-id']

class getFecha(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateTimeField()
    def __str__(self):
        return f"{self.fecha_inicio}/{self.fecha_fin}"
    
# web_quedadas/models.py
from django.db import models
from django.contrib.auth.models import User

   

class Quedada(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de clave primaria automático
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quedadas_creadas')
    participantes = models.ManyToManyField(User, related_name='quedadas_participantes')
    
    class Meta:
        app_label = 'web_quedadas'

    def __str__(self):
        return self.nombre


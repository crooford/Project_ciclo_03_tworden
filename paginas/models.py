from tkinter import CASCADE
from django.db import models

# Create your models here.
class Menu(models.Model):  
    id = models.AutoField(primary_key=True)
    nombre_plato= models.CharField(max_length=155, blank=False, null=False)
    precio= models.FloatField(null=False, blank=False)
    descripcion= models.TextField(max_length=255, blank=True, null=True)
    tipo_plato= models.CharField (
        max_length=50,
        choices=[('Entrada', 'Entrada'), ('Plato Principal', 'Plato Principal'), ('Postre', 'Postre'), ('Bebida', 'Bebida'), ('Otro', 'Otro')]                                             
    )

    def __str__(self):
        mostrar= self.nombre_plato
        return mostrar

class Mesas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_mesa= models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.nombre_mesa

class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesas,on_delete=models.CASCADE) 
    plato= models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False)
    observacion = models.TextField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.id
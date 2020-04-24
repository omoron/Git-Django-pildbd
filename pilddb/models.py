from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombres = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 75)
    email = models.EmailField(blank = True, null = True, verbose_name = 'Correo electrónico')
    telefono = models.CharField(max_length = 15)
    
class Articulos(models.Model):
    nombres = models.CharField(max_length = 50)
    seccion = models.CharField(max_length = 20)
    precio = models.IntegerField()

    #def __str__(self):
    #    return '%s, %s, %s' % (self.nombres, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

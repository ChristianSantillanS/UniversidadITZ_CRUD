from django.db import models

# Create your models here.
#Creacion de la base de datos
class Alumnos(models.Model):
    No_control = models.BigIntegerField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellido_p = models.CharField(max_length=30)
    Apellido_m = models.CharField(max_length=30)
    correo = models.CharField(max_length=60)
    img = models.FileField()

    def __str__(self):
        texto = "{0} {1} {2} "
        return texto.format(self.Nombres,self.Apellido_p, self.Apellido_m)

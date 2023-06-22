from django.db import models

# Create your models here.

class usuarios(models.Model):
    usuario = models.CharField(max_length=10)
    correo = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)

    def str(self) -> str:
        return self.usuario

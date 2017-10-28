from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MiUsuario(models.Model):
    foto = models.CharField(max_length=100, null=True)
    estado= models.CharField(max_length=300, null=True)
    usuario_django = models.OneToOneField(User, on_delete = models.CASCADE)

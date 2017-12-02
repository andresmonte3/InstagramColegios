from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class MiUsuario(models.Model):
    foto = models.CharField(max_length=100, null=True)
    estado= models.CharField(max_length=300, null=True)
    usuario_django = models.OneToOneField(User, on_delete = models.CASCADE)

class Post(models.Model):

    photo = models.CharField(max_length = 100)
    descripcion = models.CharField (max_length = 2000)
    fecha = models.DateTimeField(default = datetime.now)
    user_id = models.ForeignKey( MiUsuario , on_delete=models.CASCADE)

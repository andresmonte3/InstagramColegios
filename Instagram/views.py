from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Instagram.models import *


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render (request, 'index.html')
    else:
        name = request.POST['nombre_completo']
        username = request.POST ['usuario']
        email = request.POST ['correo']
        password = request.POST ['password']
        print (name)
        print (username)
        print (email)
        print (password)
        usuarioDjango = User.objects.create_user(username = username, password = password, email = email, first_name = name)
        miUsuario = MiUsuario( usuario_django = usuarioDjango)
        usuarioDjango.save()
        miUsuario.save()
        return redirect ('login')

def login(request):
    print (MiUsuario.objects.count())
    return render (request, 'login.html')

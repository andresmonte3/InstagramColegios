from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
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


@login_required
def home(request):
    return render (request, 'home.html')

@login_required
def profile(request):
    curr_user = request.user
    mi_usuario = MiUsuario.objects.get ( pk = request.user.pk)
    post_user = Post.objects.filter (user_id = curr_user.id)
    context={ 'usuario_actual': mi_usuario, 'post_user': post_user }
    return render (request, 'profile.html', context)

@login_required
def photos(request):
    if request.method == 'GET':
        return render(request, 'photos.html')
    else:
            photo = request.FILES ["photo"]
            fs = FileSystemStorage()
            curr_user = request.user;
            cantidad_post = Post.objects.filter(user_id = curr_user.id).count();
            name = curr_user.username + '-' + str(cantidad_post);
            filename = fs.save (name, photo)
            path = fs.url(filename)
            descripcion = request.POST['descripcion']
            newPost = Post (photo= path , descripcion= descripcion, user_id = curr_user)
            newPost.save()
            return redirect('profile')

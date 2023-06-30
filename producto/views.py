from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import produForm
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return  render(request, 'home.html')

def signup(request):
    
    if request.method =='GET':
        return render (request, 'signup.html', {
            'form': UserCreationForm
        })
    
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('productos')
           except IntegrityError:
               return render (request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        
        return render (request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'La contraseña no coincide'
                })
    
@login_required
def producto(request):
    productos = Producto.objects.filter()
    return render(request, 'productos.html', {'productos': productos})

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': produForm
        })
    else:
        try:
            form = produForm(request.POST)
            new_task = form.save(commit=False)
            new_task.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': produForm,
                #'error': 'Por favor ingrese datos validos'
            })
            
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Producto, pk=task_id)
        form = produForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Producto, pk=task_id)
            form = produForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('productos')
            else:
                return render(request, 'task_detail.html', {'task': task, 'form': form})
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': "Error actualizando producto"})
            
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Producto, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('productos')
    
    




@login_required
def signout (request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
        
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
             return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecto'
        })
        else:
            login(request, user)
            return redirect('productos')
        
from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


@login_required(login_url='/auth/login/')
def home(request):
    id = request.session['usuario']
    livros = Livros.objects.filter(usuario_id=id)
    return render(request, 'home.html', {'livros': livros})

    
@login_required(login_url='/auth/login/')
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)

    return render(request, 'ver_livro.html', {'livro': livro})

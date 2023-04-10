from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/?status=2')
def home(request):
    id = request.session['usuario']
    livros = Livros.objects.filter(usuario_id=id)
    return render(request, 'home.html', {'livros': livros})


@login_required(login_url='/auth/login/?status=2')
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)

    if request.session.get('usuario') == livro.usuario_id:
        categorias = Categoria.objects.filter(usuario_id=request.session.get('usuario'))
        emprestimos = Emprestimos.objects.filter(livro=livro)
        context = {
            'livro': livro, 
            'categorias': categorias, 
            'emprestimos': emprestimos
        }
        return render(request, 'ver_livro.html', context)
    else:
        livro = 'Não existe id de livro para esse usuário'
        return render(request, 'ver_livro.html', {'livro': livro})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from django.contrib.auth.decorators import login_required
from .forms import CadastroLivroForm


@login_required(login_url='/auth/login/?status=2')
def home(request):
    id = request.session['usuario']
    livros = Livros.objects.filter(usuario_id=id)
    form = CadastroLivroForm()
    form.fields['usuario'].initial = request.session['usuario']
    form.fields['categoria'].queryset = Categoria.objects.filter(
        usuario=request.session['usuario'])
    context = {
        'livros': livros,
        'usuario_logado': request.session['usuario'],
        'form': form
    }
    return render(request, 'home.html', context)


@login_required(login_url='/auth/login/?status=2')
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)
    if request.session.get('usuario') == livro.usuario_id:
        form = CadastroLivroForm()
        form.fields['categoria'].queryset = Categoria.objects.filter(
            usuario=request.session['usuario'])
        emprestimos = Emprestimos.objects.filter(livro=livro)
        context = {
            'livro': livro,
            'emprestimos': emprestimos,
            'usuario_logado': request.session['usuario'],
            'form': form
        }
        return render(request, 'ver_livro.html', context)
    else:
        livro = 'Não existe esse livro para esse usuário'
        return render(request, 'ver_livro.html', {'livro': livro})


@login_required(login_url='/auth/login/?status=2')
def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/livro/home/')
        else:
            return HttpResponse('Dados inválidos')


@login_required(login_url='/auth/login/?status=2')
def excluir_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect("/livro/home/")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login as log
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')

    try:
        user = get_object_or_404(Usuario, email=email)
        return redirect('/auth/cadastro/?status=3')
    except:
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/auth/cadastro/?status=1')
        if len(senha) < 8:
            return redirect('/auth/cadastro/?status=2')
        usuario = Usuario()
        usuario.username = nome
        usuario.email = email
        usuario.password = make_password(senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('password')

    user = authenticate(request, email=email, password=senha)

    if user:
        log(request, user)
        request.session['usuario'] = user.id
        return redirect(f'/livro/home/?id_usuario={request.session["usuario"]}', {'user': user})

    else:
        return redirect('/auth/login/?status=1')


def sair(request):
    request.session.flush()
    return redirect('/auth/login/')

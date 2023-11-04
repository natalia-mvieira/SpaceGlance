from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_usuario = form['nome_usuario'].value()
            senha = form['senha'].value()
        
        usuario = auth.authenticate(request, username=nome_usuario, password=senha)

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request,f'{nome_usuario} logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request,'Usuário ou senha incorretos.')
            return redirect('login')
        
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value():
                messages.error(request, 'Senhas não são iguais.')
                return redirect('cadastro')
            
            usuario = form['nome_usuario'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse usuário já existe.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(username=usuario, email=email, password=senha)
            usuario.save()
            messages.success(request, 'Cadastro criado com sucesso!')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

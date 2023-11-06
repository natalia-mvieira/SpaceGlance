from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):   
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # o '-' em data_fotografia inverte a ordem
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(legenda__icontains=nome_a_buscar) | fotografias.filter(nome__icontains=nome_a_buscar)        
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    
    fotografia = Fotografia()
    fotografia.usuario = request.user
    form = FotografiaForms(instance=fotografia)
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid:
            form.save()
            messages.success(request, 'Imagem publicada com sucesso!')
            return redirect('home')
        else: 
            messages.error(request, 'Algo deu errado, tente novamente.')
            return redirect('nova_imagem')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.usuario = request.user
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('home')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia removida com sucesso!')
    return redirect('home')
        

def tag(request,foto_tag):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True, categoria=foto_tag)
    return render(request, 'galeria/buscar.html', {'cards': fotografias})



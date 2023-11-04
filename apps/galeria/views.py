from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):   
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):    
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)        
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    
    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            form.user = request.user
            messages.success(request, 'Imagem publicada com sucesso!')
            return redirect('home')
        else: 
            messages.error(request, 'Algo deu errado, tente novamente.')
            return redirect('nova_imagem')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    return render(request, 'galeria/editar_imagem.html')

def deletar_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize o login.')
        return redirect('login')
    return render(request, 'galeria/deletar_imagem.html')




# def tag(request,categoria):
#     fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
#     if categoria=='nebulosa':
#         fotografias = fotografias.filter(categoria='Nebulosa')
#     elif categoria=='planeta':    
#         fotografias = fotografias.filter(categoria='Planeta')
#     elif categoria=='estrela':
#         fotografias = fotografias.filter(categoria='Estrela')
#     elif categoria=='galaxia':    
#         fotografias = fotografias.filter(categoria='Galáxia')
#     return render(request, 'galeria/busca_tags.html', {'cards': fotografias})



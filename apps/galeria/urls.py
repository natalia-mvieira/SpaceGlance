from django.urls import path
from apps.galeria.views import index, imagem, buscar, editar_imagem, nova_imagem, deletar_imagem, tag

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar_imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar_imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('tag/<str:foto_tag>', tag, name='tag')
]
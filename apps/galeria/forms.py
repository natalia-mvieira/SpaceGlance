from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', 'data_fotografia', 'usuario']
        labels = {'nome': 'Nome da Imagem', 'descricao': 'Descrição'}
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nebulosa de Carina'}),
            'legenda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imagem tirada do telescópio Hubble.'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Insira aqui mais detalhes sobre a sua imagem.'}),
            'foto': forms.FileInput(attrs={'class':'form-control'})}
    
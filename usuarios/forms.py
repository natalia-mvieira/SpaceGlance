from django import forms

class LoginForms(forms.Form):
    nome_usuario = forms.CharField(label='Nome de Usuário:', required=True, max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control', 
                                                               'placeholder': 'joao_silva'}))
    senha = forms.CharField(label='Senha:', required=True, max_length=20, 
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'Digite a sua senha.'}))
    
class CadastroForms(forms.Form):
    nome_usuario = forms.CharField(label='Nome de Usuário:', required=True, max_length=50,
                                 widget=forms.TextInput(attrs={'class':'form-control', 
                                                               'placeholder': 'joao_silva'}))
    email = forms.EmailField(label='E-mail:', required=True, max_length=100,
                                 widget=forms.EmailInput(attrs={'class':'form-control', 
                                                               'placeholder': 'joaosilva@email.com'}))
    senha = forms.CharField(label='Senha:', required=True, max_length=20, 
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'Digite a sua senha.'}))
    confirmar_senha = forms.CharField(label='Confirme a Senha:', required=True, max_length=20, 
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'Digite a sua senha novamente.'}))

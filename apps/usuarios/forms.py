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

    def clean_nome_usuario(self):
        nome = self.cleaned_data.get('nome_usuario')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços.')
            else:
                return nome

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas são diferentes.')
            else:
                return confirmar_senha
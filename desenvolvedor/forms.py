from desenvolvedor.models import Desenvolvedor
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class RegistroForm(ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = ['nome', 'email', 'senha']
        widgets = {'nome': TextInput(attrs={'class': 'form-control'}),
                   'email': EmailInput(attrs={'class': 'form-control'}),
                   'senha': PasswordInput(attrs={'class': 'form-control'})}


class LoginForm(ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = ['email', 'senha']
        widgets = {'email': EmailInput(attrs={'class': 'form-control'}),
                   'senha': PasswordInput(attrs={'class': 'form-control'})}
        exclude = ['nome']

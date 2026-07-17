from django import forms
from django.contrib.auth.forms import AuthenticationForm

class FormularioLoginCliente(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class': 'input-controle form-control',
            'placeholder': 'E-mail ou usuário'
        })
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={
            'class': 'input-controle form-control',
            'placeholder': 'Digite a sua senha'
        })
    )
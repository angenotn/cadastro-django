from django import forms 
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['login', 'senha', 'data_de_nascimento']
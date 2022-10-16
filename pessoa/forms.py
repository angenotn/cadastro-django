from django import forms 
from .models import Pessoa
from django.contrib.auth.forms import UserCreationForm

class PessoaForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(),
        blank = True,        
    )
    data_de_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"}
        )            
    )
    class Meta:        
        model = Pessoa
        fields = ['login', 'senha', 'data_de_nascimento']
    def __unicode__(self):
        return self.pessoa
    def __str__(self):
        return self.pessoa


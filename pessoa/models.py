from django.db import models

class Pessoa(models.Model):
    login = models.CharField(max_length = 256)
    senha = models.CharField(max_length = 256, blank = True)
    data_de_nascimento = models.DateField()     

def __str__(self) -> str:
    return self().login
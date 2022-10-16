from django.urls import path
from .views import ListaPessoaView, PessoaCreateView
from django.contrib.auth.decorators import login_required
urlpatterns = [ 
    path('', login_required(ListaPessoaView.as_view()), name = 'pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name = 'pessoa.novo')
]
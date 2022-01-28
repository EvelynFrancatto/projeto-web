# from django.shortcuts import render
# from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
    
# Create your views here.

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    model = User
    fields = ['username', 'email', 'password']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context




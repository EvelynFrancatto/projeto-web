from django.forms.models import fields_for_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Animal, Alimentacao, Higienizacao, Lugar

from django.urls import reverse_lazy


class AnimalCreate(CreateView):
    model = Animal
    fields = ['raca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AlimentacaoCreate(CreateView):
    model = Alimentacao
    fields = ['alimentacao', 'racao', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class HigienizacaoCreate(CreateView):
    model = Higienizacao
    fields = ['limpeza', 'cuidados']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class LugarCreate(CreateView):
    model = Lugar
    fields = ['espaco', 'brinquedos']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


################ UPDATE ###############

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['raca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AlimentacaoUpdate(UpdateView):
    model = Alimentacao
    fields = ['alimentacao', 'racao', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url= reverse_lazy('index')

class HigienizacaoUpdate(UpdateView):
    model = Higienizacao
    fields = ['limpeza', 'cuidados']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    
class LugarUpdate(UpdateView):
    model = Lugar
    fields = ['espaco', 'brinquedos']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


################## DELETE ##################

class AnimalDelete(DeleteView):
    model = Animal
    fields = ['raca']
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listarUsuario')

class AlimentacaoDelete(DeleteView):
    model = Alimentacao
    fields = ['alimentacao', 'racao', 'quantidade']
    template_name = 'cadastros/form-excluir.html'
    success_url= reverse_lazy('listarUsuario')

class HigienizacaoDelete(DeleteView):
    model = Higienizacao
    fields = ['limpeza', 'cuidados']
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listarUsuario')

    
class LugarDelete(DeleteView):
    model = Lugar
    fields = ['espaco', 'brinquedos']
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listarUsuario')

########### LIST ############


class AnimalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Animal
    template_name = 'cadastros/listas/animal.html'

class AlimentacaoList(ListView):
    model = Alimentacao
    template_name = 'cadastros/listas/alimentacao.html'

class HigienizacaoList(ListView):
    model = Higienizacao
    template_name = 'cadastros/listas/higienizacao.html'

class LugarList(ListView):
    model = Lugar
    template_name = 'cadastros/listas/lugar.html'


############# LOGIN #############


class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

class AlimentacaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

class HigienizacaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

class LugarUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')


# Create your views here.

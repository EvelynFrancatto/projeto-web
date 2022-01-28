from django.urls import path

from .views import AnimalCreate, AlimentacaoCreate, HigienizacaoCreate, LugarCreate
from .views import AnimalUpdate, AlimentacaoUpdate, HigienizacaoUpdate, LugarUpdate
from .views import AnimalDelete, AlimentacaoDelete, HigienizacaoDelete, LugarDelete

from .views import AnimalList, AlimentacaoList, HigienizacaoList, LugarList
urlpatterns = [ 
    path('cadastrar/animal/', AnimalCreate.as_view(), name="cadastrar-animal"),
    path('cadastrar/alimentacao/', AlimentacaoCreate.as_view(), name="cadastrar-alimentacao"),
    path('cadastrar/higienizacao/', HigienizacaoCreate.as_view(), name="cadastrar-higienizacao"),
    path('cadastrar/lugar/', LugarCreate.as_view(), name="cadastrar-lugar"),
   
    path('editar/animal/<int:pk>/', AnimalUpdate.as_view(), name="editar-animal"),
    path('editar/alimentacao/<int:pk>/', AlimentacaoUpdate.as_view(), name="editar-alimentacao"),
    path('editar/higienizacao/<int:pk>/', HigienizacaoUpdate.as_view(), name="editar-higienizacao"),
    path('editar/lugar/<int:pk>/', LugarUpdate.as_view(), name="editar-lugar"),
    
    path('excluir/animal/<int:pk>/', AnimalDelete.as_view(), name="excluir-animal"),
    path('excluir/alimentacao/<int:pk>/', AlimentacaoDelete.as_view(), name="excluir-alimentacao"),
    path('excluir/higienizacao/<int:pk>/', HigienizacaoDelete.as_view(), name="excluir-higienizacao"),
    path('excluir/lugar/<int:pk>/', LugarDelete.as_view(), name="excluir-lugar"),

    path('listar/animal/', AnimalList.as_view(), name="listar-animal"),
    path('listar/alimentacao/', AlimentacaoList.as_view(), name="listar-alimentacao"),
    path('listar/higienizacao/', HigienizacaoList.as_view(), name="listar-higienizacao"),
    path('listar/lugar/', LugarList.as_view(), name="listar-lugar"),
    
]
    
    
    
    
    
    
    
    
    
    
    

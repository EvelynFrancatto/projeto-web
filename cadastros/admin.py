from django.contrib import admin
from .models import  Animal, Alimentacao, Higienizacao, Lugar

# Register your models here.


admin.site.register(Animal)
admin.site.register(Alimentacao)
admin.site.register(Higienizacao)
admin.site.register(Lugar)



from django.db import models

# Create your models here.

# class Usuario(models.Model):
#     nome = models.charField(max_length=50)
#     email = models.charField(max_length=150)
#     senha = models.charField(max_length=25)

#     def __str__(self):
#         return "{} ({})".format(self.nome, self.email, self.senha)

class Animal(models.Model):
    raca = models.CharField(max_length=50, verbose_name="Raça")

    def __str__(self):
        return (self.raca)

class Alimentacao(models.Model):
    alimentacao = models.CharField(max_length=100, verbose_name="Tipo de Alimentação")
    racao = models.CharField(max_length=100, verbose_name="Ração")
    quantidade = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)


    def __str__(self):
        return self.alimentacao  + " - " +  self.racao  + " - " + self.quantidade

class Higienizacao(models.Model):
    limpeza = models.CharField(max_length=100)
    cuidados = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.limpeza, self.cuidados)

class Lugar(models.Model):
    espaco = models.CharField(max_length=100, verbose_name="Espaço")
    brinquedos = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.espaco, self.brinquedos)





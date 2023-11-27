from django.db import models

# Create your models here.

class Espaco(models.Model):
    id_espaco = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    descricao =models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome
    
class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    id_espaco = models.ForeignKey(
        Espaco, on_delete=models.SET_NULL, null=True
    )
    tombo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.descricao

class Servidores(models.Model):
    id_servidor = models.AutoField(primary_key=True)
    id_espaco = models.ForeignKey(
        Espaco, on_delete=models.SET_NULL, null=True
    )
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    num_telefone = models.CharField(max_length=50)
    siape = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome

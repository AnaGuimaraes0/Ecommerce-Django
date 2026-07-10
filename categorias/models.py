from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()

class Produto(models.Model):
    produto = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

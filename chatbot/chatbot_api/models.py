from django.db import models

class Resposta(models.Model):
    id = models.IntegerField()
    valor = models.CharField(max_length=1)
    descricao = models.TextField()
    acao = models.TextField()

class Resposta(models.Model):
    id = models.IntegerField()
    titulo = models.TextField()
    respostas = models.ManyToManyField(Resposta)
    acao_anterior = models.TextField()
    acao_principal = models.TextField()
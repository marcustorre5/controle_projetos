from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()  # Adicionando o campo data_inicio
    data_fim = models.DateField()  # Adicionando o campo data_fim

    def __str__(self):
        return self.nome

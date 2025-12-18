from django.db import models

class Movel(models.Model):
    nome = models.CharField(max_length=100)
    comodo = models.CharField(max_length=50)
    preco = models.FloatField()
    data_compra = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome
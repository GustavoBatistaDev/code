from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class Avaliacao(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('E', 'Excelente'),
    )

    status = models.CharField(
        choices=choices, blank=False, null=False, max_length=1, default='P'
    )

    data = models.DateTimeField(default=datetime.now)


class Anotacao(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    choices = (
        ('P', 'Positivo'),
        ('N', 'Negativo'),
    )

    tipo = models.CharField(
        choices=choices, blank=False, null=False, max_length=1, default='P'
    )
    anotacao = models.TextField()


class AlertaDeCrise(models.Model):

    choices = (
        ('P', 'Pânico'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
    )
    tipo = models.CharField(
        choices=choices, null=True, blank=True, max_length=1, default='A'
    )

    inicio = models.DateTimeField()
    fim = models.DateField(blank=True, null=True)

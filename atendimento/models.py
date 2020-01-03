from django.db import models

from paciente.models import Paciente
from profissional.models import Profissional


class Atendimento(models.Model):

    SOLUCAO_CHOICES = (
        ('implante coclear', 'Implante Coclear'),
        ('implante osseo', 'Implante Osseo/Integrado'),
        ('aasi', 'AASI'),
        ('Karina', 'AASI + IC'),
    )
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    dt_atendimento = models.DateTimeField(
        'data atendimento',
        auto_now_add=True
    )

    tipo = models.CharField(
        'tipo atendimento',
        max_length=100,
        blank=True,
        null=True
    )

    local = models.CharField(
        'local atendimento',
        max_length=100,
        blank=True,
        null=True
    )

    solucao = models.CharField(
        'tipo solucao',
        choices=SOLUCAO_CHOICES,
        max_length=100,
        blank=True,
        null=True
    )

    objetos = models.Manager()
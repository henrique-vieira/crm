from datetime import timezone

from django.db import models
from django.utils.timezone import now

from profissional.models import Profissional

class Paciente(models.Model):

    SEXO_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    STATE_CHOICES = (
        ('ac', 'Acre'),
        ('al', 'Alagoas'),
        ('ap', 'Amapá'),
        ('am', 'Amazonas'),
        ('ba', 'Bahia'),
        ('ce', 'Ceará'),
        ('df', 'Distrito Federal'),
        ('es', 'Espírito Santo'),
        ('go', 'Goiás'),
        ('ma', 'Maranhão'),
        ('mt', 'Mato Grosso'),
        ('ms', 'Mato Grosso do Sul'),
        ('mg', 'Minas Gerais'),
        ('pa', 'Pará'),
        ('pb', 'Paraíba'),
        ('pr', 'Paraná'),
        ('pe', 'Pernambuco'),
        ('pi', 'Piauí'),
        ('rj', 'Rio de Janeiro'),
        ('rn', 'Rio Grande do Norte'),
        ('rs', 'Rio Grande do Sul'),
        ('ro', 'Rondônia'),
        ('rr', 'Roraima'),
        ('sc', 'Santa Catarina'),
        ('sp', 'São Paulo'),
        ('se', 'Sergipe'),
        ('to', 'Tocantins')
    )

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    data_nascimento = models.DateField(
        'Data de Nascimento',
        null=True,
        blank=True
    )

    responsavel = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        null=True,
        blank=True
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField(
        'RG',
        max_length=11,
        null=True,
        blank=True
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    active = models.BooleanField(
        'ativo',
        default=True
    )

    blocked = models.BooleanField(
        'bloqueado',
        default=False
    )

    created = models.DateTimeField(
        'criado em',
        auto_now_add=True
    )

    modified = models.DateTimeField(
        'modificado em',
        auto_now=True
    )

    endereco = models.CharField(
        u'endereço',
        max_length=100,
        blank=True
    )

    numero = models.CharField(
        'numero',
        max_length=20,
        blank=True,
        null=True
    )

    complemento = models.CharField(
        'complemento',
        max_length=100,
        blank=True
    )

    bairro = models.CharField(
        'bairro',
        max_length=100,
        blank=True
    )

    cidade = models.CharField(
        'cidade',
        max_length=100,
        blank=True
    )

    uf = models.CharField(
        'UF', max_length=2,
        choices=STATE_CHOICES,
        blank=True
    )
    cep = models.CharField(
        'CEP',
        max_length=9,
        blank=True
    )
    def __str__(self):
        return "{}  {} ".format(self.nome, self.sobrenome)

objetos = models.Manager()
from django.db import models


class Profissional(models.Model):

    ESPECIALIDADE = (
        ('f','Fonoaudiologo'),
        ('p','Psicologo'),
        ('n','Neurologista')
    )

    crm = models.CharField(
        max_length=255,
        null=False,
        blank=False
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

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    fone = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    celular = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    especialidade = models.CharField(
        'especialidade',
        max_length=1,
        choices=ESPECIALIDADE,
        default='f',
        null=False,
        blank=False
    )

    def __str__(self):
        return "{}  {} ".format(self.nome, self.sobrenome)

    class Meta:
        verbose_name_plural = "profissionais"


    objetos = models.Manager()
from django.db import models
from django.utils.safestring import mark_safe

from paciente.models import Paciente


class Historico(models.Model):

    CHOICE_USO = (
        ('sim','SIM'),
        ('nao','NAO')
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        blank=True,
        null=True

    )

    uso_aparelho = models.CharField(
        'Ja usou AASI?',
        max_length=3,
        choices=CHOICE_USO,
        blank=True,
        null=True
    )

    tempo_uso = models.DateField(
        'Desde quando',
        auto_now=False
    )

    fabricante = models.CharField(
        'Fabricante',
        max_length=100,
        blank=True,
        null=True
    )

    tecnologia = models.CharField(
        'Tecnologia',
        max_length=100,
        blank=True,
        null=True
    )

    dt_iprf = models.DateField(
        'Data Av. Audiologica',
        auto_now=False
    )

    dt_tpf = models.DateField(
        'Data AV. Campo Livre',
        auto_now=False
    )

    mono_od = models.CharField(
        'Mono OD %',
        max_length=10,
        blank=True,
        null=True
    )

    mono_oe = models.CharField(
        'Mono OE %',
        max_length=10,
        blank=True,
        null=True
    )

    mono_od_db = models.CharField(
        'Mono OD dB',
        max_length=10,
        blank=True,
        null=True
    )

    mono_oe_db = models.CharField(
        'Mono OE dB',
        max_length=10,
        blank=True,
        null=True
    )

    dis_od = models.CharField(
        'Dis OD %',
        max_length=10,
        blank=True,
        null=True
    )

    dis_oe = models.CharField(
        'Dis OE %',
        max_length=10,
        blank=True,
        null=True
    )

    dis_od_db = models.CharField(
        'Dis OD dB',
        max_length=10,
        blank=True,
        null=True
    )

    dis_oe_db = models.CharField(
        'Dis OE dB',
        max_length=10,
        blank=True,
        null=True
    )

    lrf_od = models.CharField(
        'LRF OD dB',
        max_length=10,
        blank=True,
        null=True
    )

    lrf_oe = models.CharField(
        'LRF OE dB',
        max_length=10,
        blank=True,
        null=True
    )

    mono_s_aasi = models.CharField(
        ' Mono s/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    mono_c_aasi = models.CharField(
        'Mono c/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    sss_s_aasi = models.CharField(
        'SSS s/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    sss_c_aasi = models.CharField(
        'SSS c/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    dis_s_aasi = models.CharField(
        'Dis. s/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    dis_c_aasi = models.CharField(
        'Dis. c/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    hhia_od_c_aasi = models.CharField(
        'HHIA OD c/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    hhia_od_s_aasi = models.CharField(
        'HHIA OD s/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    hhia_oe_c_aasi = models.CharField(
        'HHIA OE c/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    hhia_oe_s_aasi = models.CharField(
        'HHIA OE s/ AASI',
        max_length=10,
        blank=True,
        null=True
    )

    img_iprf = models.ImageField(
        'Nivel de audicao IPRF',
        upload_to='website/img/',
        blank=True,
        null=True
    )

    img_tpf = models.ImageField(
        'Nivel de audicao TPF',
        upload_to='website/img/',
        blank=True,
        null=True
    )

    def __str__(self):
        return "{}".format(self.paciente)

    def image_iprf(self):
       return mark_safe('<img src="/media/%s" width="250" height="250" />' % (self.img_iprf))

       image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "historicos audiologicos"


    objetos = models.Manager()
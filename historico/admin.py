from django.contrib import admin
from django.forms import TextInput

from paciente.models import Paciente
from historico.models import Historico
from .models import *

class HistoricoAdmin(admin.ModelAdmin):

    list_filter = ('tempo_uso','fabricante','tecnologia')

    list_display = ('paciente', 'uso_aparelho', 'tempo_uso','fabricante','tecnologia','image_iprf','img_tpf')

    search_fields = ('paciente','tempo_uso','fabricante','tecnologia')

    fieldsets = (
        (None, {
            'fields': (('paciente','uso_aparelho', 'tempo_uso'), ('fabricante','tecnologia'))
        }),
        ('Avaliacao Audiologica - IPRF', {
            'fields': ('dt_iprf',('mono_od','mono_od_db'),('mono_oe','mono_oe_db'),('dis_od','dis_od_db'),
                       ('dis_oe','dis_oe_db'),('lrf_od','lrf_oe'),'img_iprf')
        }),
        ('Avaliacao em Campo Livre - TPF', {
            'fields': ('dt_tpf',('mono_s_aasi', 'mono_c_aasi'), ('sss_s_aasi', 'sss_c_aasi'), ('dis_s_aasi', 'dis_c_aasi'),'img_tpf')
        }),
        ('Questionário de Auto-Avaliacao', {
            'fields': (('hhia_od_c_aasi', 'hhia_od_s_aasi'), ('hhia_oe_c_aasi', 'hhia_oe_s_aasi'))
        }),
    )

admin.site.register(Historico,HistoricoAdmin)
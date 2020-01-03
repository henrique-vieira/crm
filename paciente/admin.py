from django.contrib import admin
from django.forms import TextInput

from paciente.models import Paciente
from django.contrib.admin.models import LogEntry,models

class PacienteAdmin(admin.ModelAdmin):

    list_filter = ('nome','profissional')

    list_display = ('nome', 'sobrenome', 'data_nascimento','created','cpf','rg','profissional')

    search_fields = ('nome','sobrenome')

    fieldsets = (
        (None, {
            'fields': (('nome', 'sobrenome'), ('sexo','data_nascimento'),'responsavel',
                       ('cpf','rg'),'profissional')
        }),
        ('Endereco', {
            'fields': (('cep','endereco'),('numero','complemento'),('bairro','cidade'),'uf')
        }),
    )


class LogEntryAdmin(admin.ModelAdmin):
    search_fields = ('object_repr',)
    list_filter = ('action_time', 'content_type',)
    list_display = ('action_time', 'user', 'content_type', 'tipo', 'object_repr')
    fields = ('action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message', )
    readonly_fields = ('action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'tipo', 'change_message', )

    def tipo(self, obj):
        if obj.is_addition():
            return u"Adicionado"
        elif obj.is_change():
            return u"Modificado"
        elif obj.is_deletion():
            return u"Deletado"

admin.site.register(LogEntry, LogEntryAdmin)

admin.site.register(Paciente, PacienteAdmin)
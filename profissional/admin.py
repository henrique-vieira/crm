from django.contrib import admin
from profissional.models import Profissional

class ProfissionalAdmin(admin.ModelAdmin):

    list_filter = ('nome', 'especialidade')

    list_display = ('nome', 'sobrenome', 'especialidade')

    search_fields = ('nome', 'especialidade')

    def upper_case_nome(self, nome):
        return ("%s" % (profissional.nome)).upper()
    upper_case_nome.short_description = 'Nome do Profissional'

    def upper_case_sobrenome(self, sobrenome):
        return ("%s" % (profissional.sobrenome)).upper()
    upper_case_sobrenome.short_description = 'Sobrenome do Profissional'

    def upper_case_especialidade(self, especialidade):
        return ("%s" % (profissional.especialidade)).upper()
    upper_case_especialidade.short_description = 'Nome do Profissional'

admin.site.register(Profissional,ProfissionalAdmin)

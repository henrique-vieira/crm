from website.views import IndexTemplateView,ProfissionalListView, ProfissionalUpdateView, ProfissionalCreateView,ProfissionalDeleteView,PacienteCreateView,PacienteListView,PacienteUpdateView,PacienteDeleteView
from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /profissional/cadastrar
    path('profissional/cadastrar', ProfissionalCreateView.as_view(), name="cadastra_profissional"),

    # GET /funcionarios
    path('profissionais/', ProfissionalListView.as_view(), name="lista_profissionais"),

    # GET/POST /profissional/{pk}
    path('profissional/<pk>', ProfissionalUpdateView.as_view(), name="atualiza_profissional"),

    # GET/POST /funcionarios/excluir/{pk}
    path('profissional/excluir/<pk>', ProfissionalDeleteView.as_view(), name="deleta_profissional"),

    # GET /paciente/cadastrar
    path('paciente/cadastrar', PacienteCreateView.as_view(), name="cadastra_paciente"),

    # GET /pacientes
    path('pacientes/', PacienteListView.as_view(), name="lista_pacientes"),

    # GET/POST /paciente/{pk}
    path('paciente/<pk>', PacienteUpdateView.as_view(), name="atualiza_paciente"),

    # GET/POST /paciente/excluir/{pk}
    path('paciente/excluir/<pk>', PacienteDeleteView.as_view(), name="deleta_paciente"),
]

from django.shortcuts import redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from profissional.models import Profissional
from paciente.models import Paciente
from website.forms import InsereProfissionalForm,InserePacienteForm



# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ProfissionalListView(ListView):
     template_name = "website/lista_profissional.html"
     model = Profissional
     context_object_name = "profissionais"


# CADASTRAMENTO DE PACIENTES
# ----------------------------------------------

class ProfissionalCreateView(CreateView):
     template_name = "website/cria_profissional.html"
     model = Profissional
     form_class = InsereProfissionalForm
     success_url = reverse_lazy("website:lista_profissionais")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ProfissionalUpdateView(UpdateView):
     template_name = "website/atualiza_profissional.html"
     model = Profissional
     fields = '__all__'
     context_object_name = 'profissional'
     success_url = reverse_lazy("website:lista_profissionais")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ProfissionalDeleteView(DeleteView):
     template_name = "website/exclui_profissional.html"
     model = Profissional
     context_object_name = 'profissional'
     success_url = reverse_lazy("website:lista_profissionais")

# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class PacienteListView(ListView):
     template_name = "website/lista_paciente.html"
     model = Paciente
     context_object_name = "pacientes"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class PacienteCreateView(CreateView):
     template_name = "website/cria_paciente.html"
     model = Paciente
     form_class = InserePacienteForm
     success_url = reverse_lazy("website:lista_pacientes")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class PacienteUpdateView(UpdateView):
     template_name = "website/atualiza_paciente.html"
     model = Paciente
     fields = '__all__'
     context_object_name = 'paciente'
     success_url = reverse_lazy("website:lista_pacientes")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class PacienteDeleteView(DeleteView):
     template_name = "website/exclui_paciente.html"
     model = Paciente
     context_object_name = 'paciente'
     success_url = reverse_lazy("website:lista_pacientes")



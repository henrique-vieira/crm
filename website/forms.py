from profissional.models import Profissional
from paciente.models import Paciente
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereProfissionalForm(forms.ModelForm):

    ESPECIALIDADE = (
        ('f', 'Fonoaudiologo'),
        ('p', 'Psicologo'),
        ('n', 'Neurologista')
    )

    especialidade = forms.ChoiceField(
        label='Especialidade',
        choices=ESPECIALIDADE,
        initial='c'
    )
    class Meta:
        # Modelo base
        model = Profissional

        # Campos que estarão no form
        fields = [
            'crm',
            'nome',
            'sobrenome',
            'cpf',
            'fone',
            'celular',
            'email',
            'especialidade'
        ]

# FORMULÁRIO DE INCLUSÃO DE PACIENTES
# -------------------------------------------

class InserePacienteForm(forms.ModelForm):

    SEXO_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    sexo = forms.ChoiceField(
        label='Sexo',
        choices=SEXO_CHOICES,
        initial='m'
    )

    class Meta:
        # Modelo base
        model = Paciente

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'rg',
            'data_nascimento',
            'responsavel',
            'sexo',
            'profissional'
        ]

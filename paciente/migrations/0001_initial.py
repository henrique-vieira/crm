# Generated by Django 3.0.1 on 2019-12-30 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissional', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='data_nascimento')),
                ('responsavel', models.CharField(max_length=255)),
                ('sexo', models.CharField(blank=True, choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('endereco', models.CharField(blank=True, max_length=100, verbose_name='endereço')),
                ('numero', models.CharField(blank=True, max_length=20, null=True, verbose_name='numero')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='complemento')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('ac', 'Acre'), ('al', 'Alagoas'), ('ap', 'Amapá'), ('am', 'Amazonas'), ('ba', 'Bahia'), ('ce', 'Ceará'), ('df', 'Distrito Federal'), ('es', 'Espírito Santo'), ('go', 'Goiás'), ('ma', 'Maranhão'), ('mt', 'Mato Grosso'), ('ms', 'Mato Grosso do Sul'), ('mg', 'Minas Gerais'), ('pa', 'Pará'), ('pb', 'Paraíba'), ('pr', 'Paraná'), ('pe', 'Pernambuco'), ('pi', 'Piauí'), ('rj', 'Rio de Janeiro'), ('rn', 'Rio Grande do Norte'), ('rs', 'Rio Grande do Sul'), ('ro', 'Rondônia'), ('rr', 'Roraima'), ('sc', 'Santa Catarina'), ('sp', 'São Paulo'), ('se', 'Sergipe'), ('to', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('profissional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profissional.Profissional')),
            ],
        ),
    ]
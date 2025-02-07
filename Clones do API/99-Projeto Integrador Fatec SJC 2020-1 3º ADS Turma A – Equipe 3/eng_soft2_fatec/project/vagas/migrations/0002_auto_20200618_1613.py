# Generated by Django 2.2 on 2020-06-18 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='competencia',
            field=models.ManyToManyField(to='vagas.Competencia', verbose_name='Competências da Vaga'),
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=20, verbose_name='Habilidades')),
                ('tipo', models.SmallIntegerField(choices=[(1, 'Hard Skills'), (2, 'Soft Skills')], verbose_name='Tipo de Habilidade')),
                ('user_add', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='vagas_habilidades_created_by', to=settings.AUTH_USER_MODEL)),
                ('user_upd', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='vagas_habilidades_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=300, verbose_name='Nome Completo')),
                ('sexo', models.SmallIntegerField(choices=[(1, 'Masculino'), (2, 'Feminino'), (3, 'Outros')], verbose_name='Gênero')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=11)),
                ('ddd', models.CharField(max_length=4, verbose_name='DDD')),
                ('celular', models.CharField(max_length=10, verbose_name='Celular')),
                ('ddd2', models.CharField(blank=True, max_length=4, null=True, verbose_name='DDD')),
                ('telefone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('rua', models.CharField(max_length=250)),
                ('bairro', models.CharField(max_length=250)),
                ('cidade', models.CharField(max_length=250)),
                ('numero_end', models.CharField(max_length=250)),
                ('complemento', models.CharField(max_length=250)),
                ('estado', models.SmallIntegerField(choices=[(1, 'Acre (AC)'), (2, 'Alagoas (AL)'), (3, 'Amapá (AP)'), (4, 'Amazonas (AM)'), (5, 'Bahia (BA)'), (6, 'Ceará (CE)'), (7, 'Distrito Federal (DF)'), (8, 'Espírito Santo (ES)'), (9, 'Goiás (GO)'), (10, 'Maranhão (MA)'), (11, 'Mato Grosso (MT)'), (12, 'Mato Grosso do Sul (MS)'), (13, 'Minas Gerais (MG)'), (14, 'Pará (PA)'), (15, 'Paraíba (PB)'), (16, 'Paraná (PR)'), (17, 'Pernambuco (PE)'), (18, 'Piauí (PI)'), (19, 'Rio de Janeiro (RJ)'), (20, 'Rio Grande do Norte (RN)'), (21, 'Rio Grande do Sul (RS)'), (22, 'Rondônia (RO)'), (23, 'Roraima (RR)'), (24, 'Santa Catarina (SC)'), (25, 'São Paulo (SP)'), (26, 'Sergipe (SE)'), (27, 'Tocantins (TO)')], verbose_name='Estado')),
                ('curriculo', models.FileField(upload_to='documents/', verbose_name='Currículo')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações sobre o candidato')),
                ('habilidades', models.ManyToManyField(to='vagas.Habilidades')),
                ('user_add', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='vagas_candidato_created_by', to=settings.AUTH_USER_MODEL)),
                ('user_upd', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='vagas_candidato_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='vaga',
            name='candidato',
            field=models.ManyToManyField(to='vagas.Candidato', verbose_name='Candidatos Cadastrados'),
        ),
    ]

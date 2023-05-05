# Generated by Django 4.0.1 on 2023-05-05 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0, unique=True)),
                ('bloco_apt', models.IntegerField(default=0, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Apartamentos',
            },
        ),
        migrations.CreateModel(
            name='Sucesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_visita', models.DateField()),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portaria.apartamento')),
            ],
            options={
                'verbose_name_plural': 'Visitantes',
            },
        ),
    ]

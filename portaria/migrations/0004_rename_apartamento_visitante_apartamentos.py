# Generated by Django 4.0.1 on 2023-05-05 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portaria', '0003_rename_tem_carro_visitante_uber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='apartamento',
            new_name='apartamentos',
        ),
    ]

# Generated by Django 4.0.6 on 2024-04-04 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_rename_idade_banda_ano_criacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banda',
            old_name='ano_criacao',
            new_name='idade',
        ),
    ]
# Generated by Django 4.0.6 on 2024-03-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_album_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='idade',
            field=models.IntegerField(verbose_name='Ano de Criação'),
        ),
    ]

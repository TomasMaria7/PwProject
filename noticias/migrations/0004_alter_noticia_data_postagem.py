# Generated by Django 4.0.6 on 2024-06-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_noticia_data_postagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Postagem'),
        ),
    ]

# Generated by Django 4.0.6 on 2024-03-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='nome',
            field=models.CharField(default='Album sem nome', max_length=100),
        ),
    ]

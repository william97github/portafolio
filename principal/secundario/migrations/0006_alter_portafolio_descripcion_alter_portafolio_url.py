# Generated by Django 4.1.3 on 2022-12-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secundario', '0005_ips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='url',
            field=models.URLField(max_length=100),
        ),
    ]

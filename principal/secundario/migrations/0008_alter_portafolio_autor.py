# Generated by Django 4.1.3 on 2022-12-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secundario', '0007_portafolio_autor_alter_portafolio_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='autor',
            field=models.CharField(max_length=50),
        ),
    ]
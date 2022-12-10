# Generated by Django 4.1.3 on 2022-12-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secundario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('etiqueta', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='persona',
        ),
    ]
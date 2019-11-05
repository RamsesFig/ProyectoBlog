# Generated by Django 2.2.6 on 2019-10-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('texto', models.CharField(max_length=1000, verbose_name='Texto')),
                ('estado', models.CharField(choices=[('DRAFT', 'Borrador'), ('Publish', 'Publicado')], default='DRAFT', max_length=200, verbose_name='Estado')),
            ],
        ),
    ]

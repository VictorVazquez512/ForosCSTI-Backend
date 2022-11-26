# Generated by Django 4.1.2 on 2022-11-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
                'db_table': 'eng_raza_cabeza',
            },
        ),
        migrations.CreateModel(
            name='Tamano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tamaño',
                'verbose_name_plural': 'Tamaños',
                'db_table': 'eng_tamano_cabeza',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'eng_tipo_cabeza',
            },
        ),
    ]
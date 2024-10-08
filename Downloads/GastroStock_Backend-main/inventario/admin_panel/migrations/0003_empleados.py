# Generated by Django 5.1 on 2024-09-06 21:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_categoria_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField(blank=True)),
                ('puesto', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_terminacion', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='empleados_fotos/')),
            ],
            options={
                'ordering': ['nombre', 'apellido'],
            },
        ),
    ]

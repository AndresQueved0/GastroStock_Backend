# Generated by Django 5.1 on 2024-09-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_pedidos_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='estado',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 5.1 on 2024-09-24 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_pedidos_pedidoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='estado',
            field=models.CharField(default='activo', max_length=10),
        ),
    ]

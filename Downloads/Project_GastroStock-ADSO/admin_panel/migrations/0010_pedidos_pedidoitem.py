# Generated by Django 5.1 on 2024-09-24 01:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_alter_categoriamenu_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plato', models.CharField(max_length=200)),
                ('precio_plato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.menuitem')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.pedidos')),
            ],
        ),
    ]

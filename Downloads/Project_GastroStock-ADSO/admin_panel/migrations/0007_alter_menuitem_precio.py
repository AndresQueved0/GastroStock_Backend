# Generated by Django 5.1 on 2024-09-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_categoriamenu_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-09 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecf_app', '0010_alter_cart_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecf_app.offer'),
        ),
    ]

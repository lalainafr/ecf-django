# Generated by Django 5.1.1 on 2025-01-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecf_app', '0017_alter_payment_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='offer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='orders',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

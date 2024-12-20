# Generated by Django 5.1.1 on 2024-12-20 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('bankName', models.CharField(blank=True, max_length=50, null=True)),
                ('accountNb', models.CharField(blank=True, max_length=50, null=True)),
                ('accountAvailable', models.FloatField(default=100.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

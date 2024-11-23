# Generated by Django 5.1.1 on 2024-11-21 21:44

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecf_app', '0004_alter_competition_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecf_app.competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartUid', models.UUIDField(default=uuid.uuid4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orders', models.ManyToManyField(to='ecf_app.order')),
            ],
        ),
    ]

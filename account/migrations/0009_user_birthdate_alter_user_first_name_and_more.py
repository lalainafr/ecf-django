# Generated by Django 5.1.1 on 2024-12-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

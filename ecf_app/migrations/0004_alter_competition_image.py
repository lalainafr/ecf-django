# Generated by Django 5.1.1 on 2024-11-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecf_app', '0003_remove_competition_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(upload_to='uploads/competition/'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitarbeiter',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

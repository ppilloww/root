# Generated by Django 5.0.4 on 2024-05-17 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0005_address_customuser_mobile_phone_customuser_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bbq_gmbh_app.address'),
        ),
    ]

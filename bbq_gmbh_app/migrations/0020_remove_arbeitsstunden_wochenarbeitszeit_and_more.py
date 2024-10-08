# Generated by Django 4.2.13 on 2024-06-01 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0019_arbeitsstunden_maxarbeitszeittag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbeitsstunden',
            name='wochenarbeitszeit',
        ),
        migrations.AddField(
            model_name='mitarbeiter',
            name='wochenarbeitszeit',
            field=models.DurationField(blank=True, choices=[(datetime.timedelta(days=1, seconds=57600), '40:00'), (datetime.timedelta(days=1, seconds=39600), '35:00'), (datetime.timedelta(days=1, seconds=21600), '30:00')], null=True),
        ),
    ]

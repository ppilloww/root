# Generated by Django 4.2.13 on 2024-06-01 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0018_arbeitsstunden_arbeitszeitges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbeitsstunden',
            name='maxArbeitszeitTag',
            field=models.DurationField(default=datetime.timedelta(seconds=36000)),
        ),
        migrations.AddField(
            model_name='arbeitsstunden',
            name='minArbeitszeitTag',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='wochenarbeitszeit',
            field=models.DurationField(blank=True, choices=[(datetime.timedelta(days=1, seconds=57600), '40:00'), (datetime.timedelta(days=1, seconds=39600), '35:00'), (datetime.timedelta(days=1, seconds=21600), '30:00')], null=True),
        ),
    ]

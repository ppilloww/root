# Generated by Django 4.2.13 on 2024-07-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0027_rename_status_urlaub_statusurlaub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlaub',
            name='vertraglicheUrlaubstage',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (25, '25'), (30, '30'), (35, '35'), (40, '40')], null=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0002_alter_mitarbeiter_gehalt_alter_mitarbeiter_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitarbeiter',
            name='ueberstunden',
            field=models.DecimalField(blank=-1, decimal_places=2, max_digits=5, null=True),
        ),
    ]

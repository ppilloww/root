# Generated by Django 4.2.13 on 2024-05-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0011_alter_arbeitsstunden_pause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='beginn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='ende',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='pause',
            field=models.DateTimeField(choices=[('01:00', '1:00'), ('00:45', '0:45'), ('00:30', '0:30'), ('00:15', '0:15'), ('00:00', '0:00')], default='01:00'),
        ),
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='stunden',
            field=models.DateTimeField(default='08:00'),
        ),
        migrations.AlterField(
            model_name='arbeitsstunden',
            name='ueberstunden',
            field=models.DateTimeField(default='00:00'),
        ),
    ]

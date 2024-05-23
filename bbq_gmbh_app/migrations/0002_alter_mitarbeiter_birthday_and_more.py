# Generated by Django 4.2.13 on 2024-05-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitarbeiter',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mitarbeiter',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mitarbeiter',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='mitarbeiter',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

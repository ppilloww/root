# Generated by Django 4.2.13 on 2024-07-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0029_alter_urlaub_beginn_alter_urlaub_ende'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitarbeiter',
            name='role',
            field=models.CharField(blank=True, choices=[('User', 'User'), ('Hr', 'HR'), ('Admin', 'Admin')], max_length=20, null=True),
        ),
    ]

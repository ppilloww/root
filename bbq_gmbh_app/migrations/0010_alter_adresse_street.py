# Generated by Django 5.0.4 on 2024-05-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0009_customuser_groups_customuser_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresse',
            name='street',
            field=models.CharField(max_length=50),
        ),
    ]

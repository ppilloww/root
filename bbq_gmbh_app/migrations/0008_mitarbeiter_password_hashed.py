# Generated by Django 5.0.4 on 2024-05-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0007_remove_mitarbeiter_admin_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitarbeiter',
            name='password_hashed',
            field=models.CharField(default='defaultpassword', max_length=255),
        ),
    ]

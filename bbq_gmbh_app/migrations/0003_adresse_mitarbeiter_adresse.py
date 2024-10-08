# Generated by Django 4.2.13 on 2024-05-26 12:35

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bbq_gmbh_app', '0002_alter_mitarbeiter_birthday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strasse', models.CharField(max_length=100)),
                ('stadt', models.CharField(max_length=100)),
                ('plz', models.CharField(max_length=10)),
                ('land', django_countries.fields.CountryField(default='DE', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='mitarbeiter',
            name='adresse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bbq_gmbh_app.adresse'),
        ),
    ]

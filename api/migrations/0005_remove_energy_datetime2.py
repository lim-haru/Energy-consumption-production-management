# Generated by Django 4.1.7 on 2023-02-17 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_datetime_energy_datetime2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energy',
            name='datetime2',
        ),
    ]
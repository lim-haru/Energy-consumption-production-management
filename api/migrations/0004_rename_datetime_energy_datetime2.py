# Generated by Django 4.1.7 on 2023-02-17 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_energy_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='energy',
            old_name='datetime',
            new_name='datetime2',
        ),
    ]

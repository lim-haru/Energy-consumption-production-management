# Generated by Django 4.1.7 on 2023-03-03 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_energy_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='energy',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='energy',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='energy',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

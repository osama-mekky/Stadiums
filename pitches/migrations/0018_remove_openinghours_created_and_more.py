# Generated by Django 4.2.7 on 2023-11-25 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0017_openinghours_created_alter_openinghours_from_hour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openinghours',
            name='created',
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 23, 55, 46, 917951)),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 23, 55, 46, 917951)),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-04 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0009_remove_pitche_city_alter_openinghours_from_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitche',
            name='city',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='pitches.city'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 16, 52, 4, 443631)),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 16, 52, 4, 443631)),
        ),
    ]
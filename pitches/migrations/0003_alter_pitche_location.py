# Generated by Django 3.2.4 on 2023-08-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0002_pitche_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitche',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]
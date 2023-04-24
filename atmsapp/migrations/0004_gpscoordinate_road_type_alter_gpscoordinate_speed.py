# Generated by Django 4.2 on 2023-04-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atmsapp', '0003_delete_pollutiondetector'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpscoordinate',
            name='road_type',
            field=models.IntegerField(choices=[(1, 'Local Street'), (2, 'Arterial'), (3, 'Highway')], null=True),
        ),
        migrations.AlterField(
            model_name='gpscoordinate',
            name='speed',
            field=models.IntegerField(null=True),
        ),
    ]

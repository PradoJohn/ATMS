# Generated by Django 4.1.3 on 2023-04-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atmsapp', '0008_gpsdevice_gpsinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpsdevice',
            name='main_function',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

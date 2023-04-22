# Generated by Django 4.2 on 2023-04-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollutionDetector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('product_model', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('Standby', 'Standby'), ('Reparing', 'Reparing'), ('Malfunctioned', 'Malfunctioned'), ('Deployed', 'Deployed')], default='Standby', max_length=255, null=True)),
            ],
        ),
    ]

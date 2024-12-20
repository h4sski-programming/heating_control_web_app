# Generated by Django 5.1.3 on 2024-11-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp_Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
            ],
        ),
    ]

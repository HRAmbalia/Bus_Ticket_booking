# Generated by Django 3.1.5 on 2021-03-25 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookTicket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busdetails',
            name='journeyDate',
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-26 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201126_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 2, 30, 10, 7725, tzinfo=utc)),
        ),
    ]

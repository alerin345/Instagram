# Generated by Django 3.1.3 on 2020-11-26 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201126_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
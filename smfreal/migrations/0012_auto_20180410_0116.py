# Generated by Django 2.0.2 on 2018-04-09 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smfreal', '0011_auto_20180410_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 19, 46, 24, 587055, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-09 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smfreal', '0014_auto_20180410_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuserdb',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 20, 6, 28, 854473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuserdb',
            name='myusername',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 20, 6, 28, 838695, tzinfo=utc)),
        ),
    ]
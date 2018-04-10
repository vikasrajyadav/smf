# Generated by Django 2.0.2 on 2018-04-09 20:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smfreal', '0018_auto_20180410_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuserdb',
            name='user_email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myuserdb',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 20, 16, 28, 113658, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 20, 16, 28, 98032, tzinfo=utc)),
        ),
    ]
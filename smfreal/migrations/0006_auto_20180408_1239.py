# Generated by Django 2.0.2 on 2018-04-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smfreal', '0005_auto_20180408_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundlist',
            name='fundno',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-08 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smfreal', '0009_fundlist_fundcomimagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundlist',
            name='fundcomimagepath',
        ),
    ]

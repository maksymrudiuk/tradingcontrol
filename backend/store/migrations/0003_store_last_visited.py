# Generated by Django 2.1 on 2019-01-09 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20181206_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='last_visited',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name='Останній візит'),
        ),
    ]

# Generated by Django 2.1 on 2019-02-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_store_last_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='work_radius',
            field=models.IntegerField(blank=True, default=500, null=True, verbose_name='Робочий радіус у м'),
        ),
    ]

# Generated by Django 2.1 on 2018-12-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Агент'), (3, 'Директор')], null=True, verbose_name='Посада'),
        ),
    ]

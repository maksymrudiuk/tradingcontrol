# Generated by Django 2.1 on 2018-11-25 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20181125_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportdata',
            old_name='assortment',
            new_name='store',
        ),
    ]

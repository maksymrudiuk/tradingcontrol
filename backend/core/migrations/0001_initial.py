# Generated by Django 2.1 on 2018-12-06 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='', verbose_name='Файл')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Завантажено')),
            ],
            options={
                'verbose_name': 'Завантажене фото',
                'verbose_name_plural': 'Завантажені фото',
            },
        ),
    ]

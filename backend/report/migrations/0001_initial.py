# Generated by Django 2.1 on 2018-12-06 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Назва')),
                ('t_start', models.CharField(max_length=5, verbose_name='Початок роботи')),
                ('t_finish', models.CharField(max_length=5, verbose_name='Кінець роботи')),
                ('t_delta', models.CharField(max_length=5, verbose_name='Тривалість роботи')),
                ('assortment_percent', models.SmallIntegerField(null=True, verbose_name='Наявність у %')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створений')),
            ],
            options={
                'verbose_name': 'Звіт',
                'verbose_name_plural': 'Звіти',
            },
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Назва')),
                ('status', models.BooleanField(verbose_name='Знайдено?')),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assortment', to='report.ReportData', verbose_name='Звіт')),
            ],
            options={
                'verbose_name': 'Товар - Звіт',
                'verbose_name_plural': 'Товари - Звіт',
            },
        ),
    ]

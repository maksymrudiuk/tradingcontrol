# Generated by Django 2.1 on 2018-11-15 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('license', models.SmallIntegerField(choices=[(1, 'Стандарт'), (3, 'Повна'), (4, 'Користувацька')], verbose_name='Ліцензія')),
            ],
            options={
                'verbose_name': 'Підриємство',
                'verbose_name_plural': 'Підприємства',
            },
        ),
        migrations.CreateModel(
            name='ContractorCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Підриємство власник')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенти',
            },
        ),
    ]

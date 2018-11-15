# Generated by Django 2.1 on 2018-11-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Назва')),
                ('image', models.ImageField(upload_to='', verbose_name='Зображення')),
                ('bar_code', models.CharField(max_length=100, verbose_name='Штрих Код')),
                ('category', models.SmallIntegerField(choices=[(1, 'Морозиво'), (3, 'Масло'), (4, 'Заморожені продукти'), (5, 'Заморожені ягоди перетерті з цукром'), (6, 'Заморожене тісто'), (7, 'Глазуровані сирки'), (8, 'Заморожена картопля та картопляні вироби'), (9, 'Заморожені напівфабрикати'), (10, 'Вафельні продукти')], default=None, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]

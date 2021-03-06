# Generated by Django 2.1 on 2019-01-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20181218_1421'),
        ('report', '0005_auto_20190125_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportitem',
            name='goods_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods_item', to='goods.Goods', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Назва'),
        ),
    ]

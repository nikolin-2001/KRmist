# Generated by Django 4.0.1 on 2022-01-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_remove_pk_image_alter_pk_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pk',
            name='haracteristick',
        ),
        migrations.AddField(
            model_name='pk',
            name='displei',
            field=models.CharField(default='', max_length=200, verbose_name='Дисплей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pk',
            name='nakopiteli',
            field=models.CharField(default=1, max_length=200, verbose_name='Дисплей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pk',
            name='operativka',
            field=models.CharField(default='', max_length=200, verbose_name='Дисплей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pk',
            name='processor',
            field=models.CharField(default=' ', max_length=200, verbose_name='Дисплей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pk',
            name='ves',
            field=models.CharField(default='', max_length=200, verbose_name='Дисплей'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0002_auto_20210908_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(),
        ),
    ]

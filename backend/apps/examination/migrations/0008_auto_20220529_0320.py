# Generated by Django 3.1.7 on 2022-05-29 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0007_auto_20211013_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата начала события'),
        ),
        migrations.AddField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата начала события'),
        ),
    ]
# Generated by Django 3.2.22 on 2023-12-22 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupindicators',
            name='indicators',
        ),
        migrations.AlterField(
            model_name='groupindicators',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Краткое наименование'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Краткое наименование'),
        ),
    ]

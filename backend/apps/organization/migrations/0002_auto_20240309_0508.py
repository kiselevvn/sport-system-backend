# Generated by Django 3.2.22 on 2024-03-09 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childgroup',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='educationgroup',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='educationgroup',
            name='description',
        ),
    ]

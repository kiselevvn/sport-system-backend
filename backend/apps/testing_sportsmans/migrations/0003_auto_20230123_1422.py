# Generated by Django 3.1.7 on 2023-01-23 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_sportsmans', '0002_auto_20230122_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test',
            new_name='test_template',
        ),
    ]

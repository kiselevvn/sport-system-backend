# Generated by Django 3.2.22 on 2023-11-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20231019_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Мужчина'), (1, 'Женщина')], null=True, verbose_name='Пол'),
        ),
    ]

# Generated by Django 3.2.22 on 2023-10-19 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birthday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='proxygroup',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='sportsman',
            options={'verbose_name': 'Спортсмен', 'verbose_name_plural': 'Спортсмены'},
        ),
    ]

# Generated by Django 3.1.7 on 2021-09-05 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0002_auto_20210905_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultExaminations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('result', models.JSONField(blank=True, null=True, verbose_name='результат обследования')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.examination', verbose_name='Обследование')),
                ('sportsman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Спортсмен')),
            ],
            options={
                'verbose_name': 'Группа обследований',
                'verbose_name_plural': 'Группы обследований',
            },
        ),
    ]
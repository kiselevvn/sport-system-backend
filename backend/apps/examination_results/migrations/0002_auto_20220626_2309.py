# Generated by Django 3.1.7 on 2022-06-26 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination_templates', '0001_initial'),
        ('examination_results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultexaminations',
            name='sportsman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Спортсмен'),
        ),
        migrations.AddField(
            model_name='groupexaminations',
            name='examinations',
            field=models.ManyToManyField(to='examination_results.Examination', verbose_name='Обследования'),
        ),
        migrations.AddField(
            model_name='examination',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='examination_results.event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='examination',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination_templates.examinationtemplate', verbose_name='Шаблон обследования'),
        ),
    ]
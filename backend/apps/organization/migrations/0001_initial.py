# Generated by Django 3.2.22 on 2024-03-03 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True, verbose_name='Наименование организации полное')),
                ('short_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Краткое наименование')),
                ('inn', models.CharField(blank=True, max_length=20, null=True, verbose_name='ИНН')),
                ('kpp', models.CharField(blank=True, max_length=20, null=True, verbose_name='КПП')),
                ('ogrn', models.CharField(blank=True, max_length=20, null=True, verbose_name='ОГРН')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='EducationGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень образования группы')),
                ('сhar_code', models.CharField(default='', max_length=6, verbose_name='Символьный код')),
                ('is_training_started', models.BooleanField(default=False, verbose_name='Начат процесс обучения')),
                ('date_training_started', models.DateField(blank=True, null=True, verbose_name='Дата начала обучения')),
                ('is_training_completed', models.BooleanField(default=False, verbose_name='Процесс обучения завершен')),
                ('date_training_completed', models.DateField(blank=True, null=True, verbose_name='Дата окончания обучения')),
                ('is_archival', models.BooleanField(blank=True, null=True, verbose_name='Является архивной')),
                ('archive_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата архивации')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='ChildGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Фактический порядковый номер')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('сhar_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Символьный код')),
                ('education_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.educationgroup', verbose_name='Группа')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Подгруппы',
            },
        ),
    ]

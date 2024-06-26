# Generated by Django 3.2.22 on 2024-02-23 23:40

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resulttest',
            old_name='test',
            new_name='test_template',
        ),
        migrations.AddField(
            model_name='resulttest',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='resulttest',
            unique_together={('test_template', 'date', 'user')},
        ),
    ]

# Generated by Django 3.2.22 on 2024-02-24 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20240224_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='resulttest',
            name='test_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_tests', to='testing.testtemplate', verbose_name='Тест'),
        ),
    ]
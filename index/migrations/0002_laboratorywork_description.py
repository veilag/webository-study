# Generated by Django 5.1.3 on 2024-11-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorywork',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
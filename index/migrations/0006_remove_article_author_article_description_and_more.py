# Generated by Django 5.1.3 on 2024-11-10 11:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='independentwork',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='independentwork',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='laboratorywork',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Контент'),
        ),
    ]

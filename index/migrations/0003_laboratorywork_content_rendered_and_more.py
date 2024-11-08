# Generated by Django 5.1.3 on 2024-11-08 15:01

import markdownfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_laboratorywork_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorywork',
            name='content_rendered',
            field=markdownfield.models.RenderedMarkdownField(default='', verbose_name='Markdown контент'),
        ),
        migrations.AlterField(
            model_name='laboratorywork',
            name='content',
            field=markdownfield.models.MarkdownField(default='', rendered_field='content_rendered'),
        ),
    ]

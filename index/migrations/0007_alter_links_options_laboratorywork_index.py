# Generated by Django 5.1.3 on 2024-11-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_article_author_article_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AddField(
            model_name='laboratorywork',
            name='index',
            field=models.IntegerField(default=1),
        ),
    ]
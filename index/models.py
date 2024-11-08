from django.db import models
from django.contrib.auth.models import User
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название предмета")

    def __str__(self):
        return self.name


class LaboratoryWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.TextField(verbose_name="Описание", default="")
    content = MarkdownField(rendered_field='content_rendered', default="", validator=VALIDATOR_STANDARD)
    content_rendered = RenderedMarkdownField(verbose_name="Markdown контент", default="")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Лабораторная работа: {self.title} ({self.subject})"


class IndependentWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    content = models.TextField(verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Самостоятельная работа: {self.title} ({self.subject})"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"Статья: {self.title} (Автор: {self.author})"

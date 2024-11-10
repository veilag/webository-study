from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название предмета")

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class LaboratoryWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.TextField(verbose_name="Описание", default="")
    content = RichTextField(default="", verbose_name="Контент")
    index = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Лабораторная работа"
        verbose_name_plural = "Лабораторные работы"

    def __str__(self):
        return f"Лабораторная работа: {self.title} ({self.subject})"


class IndependentWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.TextField(verbose_name="Описание", default="")
    content = RichTextField(verbose_name="Контент")
    index = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Самостоятельная работа"
        verbose_name_plural = "Самостоятельные работы"

    def __str__(self):
        return f"Самостоятельная работа: {self.title} ({self.subject})"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", default="")
    content = RichTextField(verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"Статья: {self.title}"


class Links(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    source = models.TextField()

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return f"Ссылка: {self.name}"

from django.contrib import admin
from django import forms
from . import models


admin.site.register(models.LaboratoryWork)
admin.site.register(models.Article)
admin.site.register(models.IndependentWork)
admin.site.register(models.Subject)
admin.site.register(models.Links)

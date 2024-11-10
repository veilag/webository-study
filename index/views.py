from django.shortcuts import render
from . import models


def index(request):
    laboratories = models.LaboratoryWork.objects.all().order_by('-index')[:5]
    independents = models.IndependentWork.objects.all().order_by('-index')[:5]
    articles = models.Article.objects.all()
    links = models.Links.objects.all()
    subjects = models.Subject.objects.all()

    return render(request, 'index/index.html', {
        'laboratories': laboratories,
        'independents': independents,
        'links': links,
        'articles': articles,
        'subjects': subjects
    })


def laboratory(request, id):
    laboratory_item = models.LaboratoryWork.objects.get(pk=id)

    return render(request, 'index/laboratory.html', {
        'laboratory': laboratory_item
    })


def subject_laboratories(request, id: int):
    subject = models.Subject.objects.get(pk=id)
    laboratories = subject.laboratorywork_set.all().order_by('-index')

    return render(request, 'index/subject_laboratories.html', {
        "subject": subject,
        "laboratories": laboratories
    })

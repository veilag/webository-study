from django.shortcuts import render
from . import models


def index(request):
    laboratories = models.LaboratoryWork.objects.all()[:5]
    independents = models.IndependentWork.objects.all()[:5]

    subjects = models.Subject.objects.all()

    return render(request, 'index/index.html', {
        'laboratories': laboratories,
        'independents': independents,
        'subjects': subjects
    })


def index_subject_filter(request, subject_id: int):
    laboratories = models.LaboratoryWork.objects.filter(subject_id=subject_id)
    subjects = models.Subject.objects.all()

    return render(request, 'index/index.html', {
        'laboratories': laboratories,
        'subjects': subjects
    })


def laboratory(request, id):
    laboratory_item = models.LaboratoryWork.objects.get(pk=id)

    return render(request, 'index/laboratory.html', {
        'laboratory': laboratory_item
    })

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models


def index(request):
    cousers = models.Course.objects.all()
    # return HttpResponse("".join([str(corser) + "<br>" for corser in cousers]))
    return render(request, 'shop/courser.html', context={'cousers': cousers})


def single_course(request, course_id):
 #   # option 1 404
 #   try:
 #       course = models.Course.objects.get(pk=course_id)
 #       return render(request, 'shop/single_course.html', {'course': course})
 #   except models.Course.DoesNotExist:
 #       raise Http404

    # option 2  404
    course = get_object_or_404(models.Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})

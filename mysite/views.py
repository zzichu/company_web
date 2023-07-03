# from django.http import HttpResponse 삭제
from django.shortcuts import render
from .models import MainContent


def index(request):
    # return HttpResponse("Hello world") 삭제

    contene_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': contene_list}
    return render(request, 'mysiite/content_list.html', context)

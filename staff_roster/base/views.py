from django.shortcuts import render, redirect
from base.models import Management


def index(request):
    if request.method == 'GET':
        return render(request, 'base/index.html')


def roster(request):
    if request.method == 'GET':
        return render(request, 'base/roster.html')


def management_list(request):
    accessible_managements = Management.objects.all()
    context = {
        'managements': accessible_managements
    }
    return render(request, 'base/management_list.html', context)

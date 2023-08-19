from django.shortcuts import render, redirect


def index(request):
    if request.method == 'GET':
        return render(request, 'base/index.html')


def roster(request):
    if request.method == 'GET':
        return render(request, 'base/roster.html')

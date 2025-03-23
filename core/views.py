from django.shortcuts import render


def home(request):
    page = 'core/home.html'
    context = {}
    return render(request, page, context)

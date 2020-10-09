from django.shortcuts import render
from django.views.generic import View


def home(request):
    return render(request, 'index.html')


# class Home(View):
#     template_name = 'index.html'

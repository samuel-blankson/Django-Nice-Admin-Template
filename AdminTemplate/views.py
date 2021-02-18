from django.shortcuts import render
from .models import Todo

# Create your views here.
todos = []


def index(request):
    return render(request, 'index.html', {'downloads': 4000})


def table(request):
    return render(request, 'basic_table.html', {'todos': todos})


def submit(request):
    return render(request, 'basic_table.html', {'todos': todos})


def search(request):

    return render(request, 'search.html', {'todos': todos})


def delete(request):

    return render(request, 'basic_table.html', {'todos': todos})


def form(request):
    return render(request, 'form_component.html')


def edit(request):
    return render(request, 'edit_form.html')

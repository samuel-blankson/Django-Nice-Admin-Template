from django.shortcuts import render
from .models import Todo

# Create your views here.


def index(request):
    return render(request, 'index.html', {'downloads': 4000})


def table(request):

    todo = Todo()
    todo.subject = 'Travel'
    todo.date = '20/2/2021'
    todo.location = 'Nigeria'
    todo.todoType = 'regular'
    todo.description = 'i am nice'

    return render(request, 'basic_table.html', {'todo': todo})


def submit(request):

    todo = Todo()

    todo.subject = 'Travel'
    todo.date = '20/2/2021'
    todo.location = 'Nigeria'
    todo.todoType = 'regular'
    todo.description = 'i am nice'
    return render(request, 'basic_table.html')


def search(request):

    todo = Todo()

    todo.subject = 'Travel'
    todo.date = '20/2/2021'
    todo.location = 'Nigeria'
    todo.todoType = 'regular'
    todo.description = 'i am nice'

    return render(request, 'search.html', {'todo': todo})


def delete(request):

    todo = Todo()

    todo.subject = 'Travel'
    todo.date = '20/2/2021'
    todo.location = 'Nigeria'
    todo.todoType = 'regular'
    todo.description = 'i am nice'

    return render(request, 'basic_table.html', {'todo': todo})


def form(request):
    return render(request, 'form_component.html')


def edit(request):
    return render(request, 'edit_form.html')

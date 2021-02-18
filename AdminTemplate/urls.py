from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('table', views.table, name='table'),
    path('form', views.form, name='form'),
    path('edit', views.edit, name='edit'),
    path('search', views.search, name='search'),
    path('delete', views.delete, name='delete'),
    path('submit', views.submit, name='submit')
]

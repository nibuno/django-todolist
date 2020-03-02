from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import ToDoList


class IndexView(ListView):

    model = ToDoList
    queryset = ToDoList.objects.order_by('-created_date')
    paginate_by = 20


class DetailView(DetailView):
    model = ToDoList


class DeleteView(DeleteView):
    model = ToDoList

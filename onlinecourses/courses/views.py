from django.shortcuts import render
from .models import Courses
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class coursesListView(ListView):
    model = Courses

class coursesDetailView(DetailView):
    model = Courses

class coursesCreateView(CreateView):
    model = Courses
    fields = '__all__'

class coursesUpdateView(UpdateView):
    model = Courses
    fields = '__all__'

class coursesDeleteView(DeleteView):
    model = Courses
    success_url = reverse_lazy('courses')


from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import Blog
from .forms import BlogForm

class BlogHomeView(ListView):
	model = Blog

class BlogCreateView(CreateView):
	model = Blog
	form_class = BlogForm

class BlogDetailView(DetailView):
	model = Blog

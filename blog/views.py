from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Blog
from django.views.generic import DetailView, ListView, TemplateView, CreateView


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "context", "image", "created_at")
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


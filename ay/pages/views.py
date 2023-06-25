from django.views import generic
from .models import Blog


class HomeView(generic.ListView):
    template_name = 'pages/index.html'
    queryset = {}


class BlogsView(generic.ListView):
    template_name = 'pages/service.html'
    queryset = {}


class BlogDetailView(generic.DetailView):
    template_name = 'pages/blog.html'
    model = Blog


class ServiceView(generic.ListView):
    template_name = 'pages/service.html'
    queryset = {}

from django.views import generic
from .models import Course


class HomeView(generic.ListView):
    template_name = 'pages/index.html'
    queryset = {}


class ServiceView(generic.ListView):
    template_name = 'pages/service.html'
    queryset = Course.objects.all()


class BlogView(generic.ListView):
    template_name = 'pages/blog.html'
    queryset = {}

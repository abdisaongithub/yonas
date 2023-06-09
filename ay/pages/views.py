from django.views import generic


class HomeView(generic.ListView):
    template_name = 'pages/index.html'
    queryset = {}


class ServiceView(generic.ListView):
    template_name = 'pages/service.html'
    queryset = {}


class BlogView(generic.ListView):
    template_name = 'pages/blog.html'
    queryset = {}

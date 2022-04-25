from django.shortcuts import render
from django.views import generic


class HomeView(generic.ListView):
    template_name = 'pages/index.html'
    queryset = {}


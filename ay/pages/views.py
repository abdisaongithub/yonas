import random

from django.shortcuts import render
from django.views import generic

from .models import Blog


def home_page(request):
    items = list(Blog.objects.translated())
    posts = random.sample(items, 2)
    return render(template_name='pages/index.html', context={'posts': posts}, request=request)


class BlogView(generic.ListView):
    template_name = 'pages/posts.html'
    queryset = Blog.objects.all()


def blog_detail(request, pk):
    post = Blog.objects.translated(pk=pk).first()
    items = list(Blog.objects.translated())
    posts = random.sample(items, 4)
    return render(request, 'pages/blog.html', {'post': post, 'posts': posts})

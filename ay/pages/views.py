from django.shortcuts import render
from django.views import generic

from .models import Blog


def home_page(request):
    posts = Blog.objects.all()
    return render(template_name='pages/index.html', context={posts: posts}, request=request)


class BlogView(generic.ListView):
    template_name = 'pages/posts.html'
    queryset = Blog.objects.all()


def blog_detail(request, pk):
    post = Blog.objects.translated(pk=pk).first()
    return render(request, 'pages/post.html', {'post': post})

from django.urls import path, include

from .views import BlogView, home_page, blog_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('posts/', BlogView.as_view(), name='blogs'),
    path('posts/<int:pk>', blog_detail, name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
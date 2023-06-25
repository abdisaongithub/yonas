from django.urls import path

from .views import HomeView, ServiceView, BlogsView, BlogDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', BlogsView.as_view(), name='posts'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('services/', ServiceView.as_view(), name='services'),
]

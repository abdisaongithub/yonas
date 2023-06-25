from django.urls import path

from .views import HomeView, ServiceView, BlogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', ServiceView.as_view(), name='posts'),
    path('services/', ServiceView.as_view(), name='services'),
    path('blog/', BlogView.as_view(), name='blog')
]

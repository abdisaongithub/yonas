from django.urls import path, include
from django.conf.urls.static import static
from .views import BlogView, home_page, blog_detail
from ay import settings

urlpatterns = [
    path('', home_page, name='home'),
    # path('posts/', BlogView.as_view(), name='blogs'),
    path('posts/<int:pk>', blog_detail, name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

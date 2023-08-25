from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Blog

# Register your models here.
admin.site.register(Blog, TranslatableAdmin)

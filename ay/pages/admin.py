from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Contact, About, Blog, BlogText, BlogImage

admin.site.register(Contact, TranslatableAdmin)
admin.site.register(About, TranslatableAdmin)
admin.site.register(Blog, TranslatableAdmin)
admin.site.register(BlogText, TranslatableAdmin)
admin.site.register(BlogImage, TranslatableAdmin)

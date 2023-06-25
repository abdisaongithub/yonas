import django.utils.datetime_safe
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Contact(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        phone=models.CharField(max_length=15),
        message=models.TextField(),
        created_at=models.DateTimeField(auto_now_add=True),
        updated_at=models.DateTimeField(auto_now=True),
    )

    def __str__(self):
        return str(self.name) + ' - ' + str(self.phone)


class BlogTag(TranslatableModel):
    translations = TranslatedFields(
        tag=models.CharField(max_length=50),
        created_at=models.DateTimeField(auto_now_add=True),
        updated_at=models.DateTimeField(auto_now=True),
    )

    def __str__(self):
        return self.tag


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        tags=models.ManyToManyField(BlogTag),
        created_at=models.DateTimeField(auto_now_add=True),
        updated_at=models.DateTimeField(auto_now=True),
    )

    def __str__(self):
        return self.title


class BlogText(TranslatableModel):
    translations = TranslatedFields(
        blog=models.ForeignKey('pages.Blog', on_delete=models.CASCADE, blank=True, null=False),
        text=models.TextField(),
        order=models.IntegerField(default=0),
        created_at=models.DateTimeField(auto_now_add=True),
        updated_at=models.DateTimeField(auto_now=True),
    )

    def __str__(self):
        return self.text[:50]


class BlogImage(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, blank=True, null=False)
    image = models.ImageField(upload_to='photos/blog/%Y/%m/%d')
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog


class About(TranslatableModel):
    translations = TranslatedFields(
        image=models.ImageField(upload_to='images/about/'),
        text=models.TextField(),
        created_at=models.DateTimeField(auto_now_add=True),
        updated_at=models.DateTimeField(auto_now=True),
    )

    def __str__(self):
        return self.text

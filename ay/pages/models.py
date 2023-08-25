from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.CharField(max_length=255, default=''),
        image=models.ImageField(upload_to='posts', blank=True, ),
        content=RichTextUploadingField(default=''),
        createdAt=models.DateTimeField(auto_now_add=True),
        updatedAt=models.DateTimeField(auto_now=True)
    )

    def __str__(self):
        return self.title


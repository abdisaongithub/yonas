from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        descricption=models.CharField(max_length=255, default=''),
        image=models.ImageField(upload_to='posts', blank=True, ),
        content=RichTextUploadingField(default='')
    )

    def __str__(self):
        return self.title


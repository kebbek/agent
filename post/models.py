from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    image = models.ImageField(upload_to='images/', default='default.png')
    title = models.CharField(max_length=40)
    content = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# models.py
from django.db import models

class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/')  # Specify the upload folder inside 'media'
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

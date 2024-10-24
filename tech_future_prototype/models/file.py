from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
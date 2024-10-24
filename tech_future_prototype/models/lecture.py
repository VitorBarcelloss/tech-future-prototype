from django.db import models


class Lecture(models.Model):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(null=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='lectures')
    files = models.ManyToManyField('Document', related_name='lecture_files')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title

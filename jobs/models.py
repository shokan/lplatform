from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class Jobs(models.Model):
    job_name = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

class OcrData(models.Model):
    job_id = models.ForeignKey(Jobs, 
                               on_delete=models.CASCADE)
    file_hash = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    upload_time = models.DateTimeField(default=timezone.now)
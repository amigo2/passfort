import uuid
from django.db import models
from simple_history.models import HistoricalRecords


class Document(models.Model):
    title = models.CharField(blank=False, max_length=50)
    date = models.DateTimeField(auto_now_add=True, )
    file = models.FileField(blank=True, null=True, upload_to='files/')
    history = HistoricalRecords()

    def __str__(self):
        return self.title

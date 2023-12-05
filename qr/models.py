# models.py
from django.db import models

class QRData(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data

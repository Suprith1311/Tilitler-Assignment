from django.db import models
from django.db.models import IntegerField
import uuid


class movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    rating = models.ImageField(upload_to='car')

    def __str__(self):
        return self.id

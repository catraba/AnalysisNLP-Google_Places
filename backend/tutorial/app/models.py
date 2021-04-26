from django.db import models

# Create your models here.

class Place(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location_id = models.PositiveIntegerField()
    title = models.CharField(max_length=30)
    url = models.TextField()
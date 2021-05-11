from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
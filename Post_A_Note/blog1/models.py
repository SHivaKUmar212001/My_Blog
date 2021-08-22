from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

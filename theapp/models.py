from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'{self.message}'
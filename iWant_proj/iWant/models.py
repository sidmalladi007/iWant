from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Wish(models.Model):
    item = models.CharField(max_length=50)
    creator = models.ForeignKey(User)
    created_date = models.DateTimeField('date published', auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return self.item

    class Meta:
        ordering = ('created_date',)
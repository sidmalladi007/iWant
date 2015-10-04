from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz

class Wish(models.Model):
    creator = models.ForeignKey(User)
    item = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, default='')
    condition = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField()
    details = models.TextField(default='')

    def __str__(self):
        return self.item

    class Meta:
        ordering = ('-created_date',)
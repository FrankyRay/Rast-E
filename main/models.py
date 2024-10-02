from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField()

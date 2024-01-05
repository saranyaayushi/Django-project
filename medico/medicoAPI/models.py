from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    expiry = models.DateField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    expiry=models.DateField()
    description=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

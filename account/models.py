from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    registe_datetime = models.DecimalField(auto_now=True)
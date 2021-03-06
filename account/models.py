from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=225)
    email = models.EmailField()
    registe_datetime = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(null=True, default=False)
    assign_store_size = models.IntegerField(default=20000)
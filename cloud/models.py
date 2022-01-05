from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT
from ..account.models import Account

# Create your models here.
class StoreFile(models.Model):
    file_path = models.FileField()
    file_name = models.CharField(max_length=300)
    create_date = models.DateField(auto_now=True)
    upload_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(Account, on_delete=CASCADE, related_name='account')


class ShareStoreFile(models.Model):
    storefile = models.ForeignKey(StoreFile, on_delete=CASCADE, related_name='storefile')
    shareuser = models.ForeignKey(Account, on_delete=SET_DEFAULT, default=0, related_name='account')
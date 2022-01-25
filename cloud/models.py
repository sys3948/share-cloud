from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT

# Create your models here.
class FileFolder(models.Model):
    folder_id = models.IntegerField(default=1)
    folder_name = models.CharField(max_length=300)
    oner_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='oner_id',)
    share_id = models.IntegerField(default=0)
    upper_folder_id = models.IntegerField()
    level = models.IntegerField(default=0)


class StoreFile(models.Model):
    file_path = models.FileField()
    file_name = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='account')
    folder_id = models.IntegerField(default=1)



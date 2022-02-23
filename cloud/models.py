from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT

# Create your models here.
class FileFolder(models.Model):
    folder_id = models.IntegerField(default=1)
    folder_name = models.CharField(max_length=300)
    oner_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='oner_id',)
    upper_folder_id = models.ForeignKey('self', on_delete=CASCADE, related_name='upper_id')
    level = models.IntegerField(default=0)
    share_able = models.BooleanField(default=False)


class StoreFile(models.Model):
    file_path = models.FileField()
    file_name = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='account')
    belong_folder_id = models.ForeignKey(FileFolder, on_delete=CASCADE, related_name='belong_folder_id')


class ShareFolder(models.Model):
    share_folder_id = models.ForeignKey(FileFolder, on_delete=CASCADE, related_name='share_folder_id')
    onner_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='onner_id')
    share_user_id = models.ForeignKey('account.Account', on_delete=CASCADE, related_name='share_id')


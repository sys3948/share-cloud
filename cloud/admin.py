from django.contrib import admin
from .models import FileFolder, StoreFile

# Register your models here.
admin.site.register(StoreFile)
admin.site.register(FileFolder)
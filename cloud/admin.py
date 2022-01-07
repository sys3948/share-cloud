from django.contrib import admin
from .models import ShareStoreFile, StoreFile

# Register your models here.
admin.site.register(StoreFile)
admin.site.register(ShareStoreFile)
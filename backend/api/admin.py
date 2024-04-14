from django.contrib import admin
from .models import QRCode, User

# Register your models here.

admin.site.register(User)
admin.site.register(QRCode)

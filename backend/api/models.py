from django.db import models
from django.contrib.auth.models import AbstractUser
from qrcode import make
from .managers import UserManager
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


class QRCode(models.Model):
    TYPES = [
        ('URL', 'URL'),
        ('TEXT', 'Text'),
        ('CONTACT', 'Contact Details'),
        ('WIFI', 'Wi-Fi Network Configuration'),
    ]
    qr_image = models.ImageField(upload_to="qr_codes", null=True, blank=True)
    qr_type = models.CharField(max_length=10, choices=TYPES)
    qr_data = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        qrcode_img = make(self.qr_data)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        qr_offset.paste(qrcode_img)
        file_name = f'qr-{self.qr_data}.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_image.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

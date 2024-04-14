# Generated by Django 4.2.4 on 2024-04-10 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('qr_type', models.CharField(choices=[('URL', 'URL'), ('TEXT', 'Text'), ('CONTACT', 'Contact Details'), ('WIFI', 'Wi-Fi Network Configuration')], max_length=10)),
                ('qr_data', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

from django import forms
from .models import QRCode

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['qr_type', 'qr_data']

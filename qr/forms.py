# forms.py
from django import forms
from .models import QRData

class QRForm(forms.ModelForm):
    class Meta:
        model = QRData
        fields = ['data']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'acceptor'}),
        }
        labels = {
            'data': 'Enter Address',  # Customize the label text
        }
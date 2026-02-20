from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class MedicalImageForm(forms.Form):
    image = forms.ImageField(label="Upload X-ray or CT Scan")


class LabReportForm(forms.Form):
    report = forms.FileField(label="Upload Lab Report (PDF or Image)")

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']


User = get_user_model()



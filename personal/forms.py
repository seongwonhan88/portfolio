from django import forms

from personal.models import ContactInfo


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 'message_type', 'message_content']

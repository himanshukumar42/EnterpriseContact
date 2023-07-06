from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'email', 'country_code', 'mobile', 'event_notification', 'event_types', 'status']
        widgets = {
            'event_notification': forms.Select(attrs={'class': 'form-control'}),
            'event_types': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


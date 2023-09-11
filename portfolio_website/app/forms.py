from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "cont", "placeholder": "Name"}),
            "email": forms.TextInput(attrs={"class": "cont", "placeholder": "Email"}),
            "subject": forms.TextInput(
                attrs={"class": "cont", "placeholder": "Subject"}
            ),
            "message": forms.TextInput(
                attrs={"class": "cont_message", "placeholder": "Message"}
            ),
        }

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    subject = forms.CharField(label="Subject", max_length=100, required=True)
    phoneno = forms.CharField(label="Phone no", max_length=100, required=True)
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Enter your message here"
        })
    )

from django import forms
from .models import Profile, ContactMessage

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'surname']

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email address')
    subject = forms.CharField(label='Subject', max_length=255)
    message = forms.CharField(label='Message', widget=forms.Textarea)

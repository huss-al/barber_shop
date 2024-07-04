from django import forms
from .models import Profile, ContactMessage, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from barbers.models import Barber 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'surname']

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email address')
    subject = forms.CharField(label='Subject', max_length=255)
    message = forms.CharField(label='Message', widget=forms.Textarea)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['notes', 'datetime', 'cut', 'barber']

        widgets = {
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'cut': forms.Select(attrs={'class': 'form-control'}),
        }
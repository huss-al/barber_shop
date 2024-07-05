from django import forms
from .models import Profile, ContactMessage, Appointment, CutType
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
    firstname = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'surname', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['surname']
        if commit:
            user.save()
            # Check if profile already exists
            profile, created = Profile.objects.get_or_create(user=user)
            if not created:
                # Update existing profile if necessary
                profile.firstname = self.cleaned_data['firstname']
                profile.surname = self.cleaned_data['surname']
                profile.save()
        return user
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['datetime', 'cut', 'barber']

        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'cut': forms.Select(attrs={'class': 'form-control'}),
            'barber': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['cut'].queryset = CutType.objects.all()
        self.fields['barber'].queryset = Barber.objects.filter(is_available=True)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, CutType, Gallery, AboutUsContent, ContactMessage, Appointment, Barber
from .forms import ProfileForm, ContactForm, BookingForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login




def home(request):
    return render(request, 'main/home.html')  # view for home.html


def services(request):
    return render(request, 'main/services.html')  # view for service.html

def services_view(request):
    cut_types = CutType.objects.all()  # Retrieve all CutType entries
    return render(request, 'main/services.html', {'cut_types': cut_types})


def gallery(request):
    return render(request, 'main/gallery.html') 

def gallery_view(request):
    images = Gallery.objects.all()  
    return render(request, 'main/gallery.html', {'images': images})


def about_us(request):
    return render(request, 'main/about_us.html')   

def about_us(request):
    content = AboutUsContent.objects.first()  # Assuming there's only one About Us content
    return render(request, 'main/about_us.html', {'content': content})


def contact_us(request):
    return render(request, 'main/contact_us.html')


def booking_page(request):
    return render(request, 'main/booking_page.html')


@login_required
def view_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'main/view_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'main/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'main/delete_profile.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            return redirect('contact_us_confirmation-page')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact_us.html', {'form': form})

def contact_us_confirmation(request):
    last_message = ContactMessage.objects.last()  # Get the last submitted message
    return render(request, 'main/contact_us_confirmation.html', {'message': last_message})



class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    
    def get_success_url(self):
        return reverse_lazy('booking-page')  # Assuming 'booking-page' is the name of your booking page URL

    def form_valid(self, form):
        # Handle form validation logic here if needed
        return super().form_valid(form)

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'main/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'main/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home-page')  # Redirect to home page or any other page after registration
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def booking_page(request):
    cut_types = CutType.objects.all()  # Fetch all CutType instances for the booking form dropdown
    barbers = Barber.objects.filter(is_available=True)  # Fetch all Barber instances for the dropdown

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user.profile
            appointment.save()
            return redirect('booking_success')  # Redirect to the success page
    else:
        form = BookingForm()

    return render(request, 'main/booking_page.html', {'form': form, 'cut_types': cut_types, 'barbers': barbers})



@login_required
def booking_success(request):
    try:
        appointment = Appointment.objects.filter(client=request.user.profile).latest('datetime')
    except Appointment.DoesNotExist:
        appointment = None

    return render(request, 'main/booking_success.html', {'appointment': appointment})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, CutType, Gallery, AboutUsContent, ContactMessage
from .forms import ProfileForm, ContactForm


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


@login_required
def view_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profiles/view_profile.html', {'profile': profile})

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
    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'profiles/delete_profile.html')


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
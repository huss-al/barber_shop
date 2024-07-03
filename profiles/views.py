from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, CutType, Gallery, AboutUsContent
from .forms import ProfileForm


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



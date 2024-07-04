from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def book_now(request):
    return render(request, 'booking_page.html')

def redirect_to_login(request):
    return redirect('login')


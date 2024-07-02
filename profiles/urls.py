from django.urls import path
from .views import home, about_us, contact_us
from . import views



urlpatterns = [
    path('', home, name='home-page'),
    path('services/', views.services_view, name='services-page'),
    path('gallery/', views.gallery_view, name='gallery-page'),
    path('about_us/', about_us, name='about_us-page'),
    path('contact_us/', contact_us, name='contact_us-page'),
]

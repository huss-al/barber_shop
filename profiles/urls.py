from django.urls import path
from .views import home, services, view_profile, edit_profile, delete_profile


urlpatterns = [
    path('', home, name='home-page'),
    path('services/', services, name='services-page'),  # Add this line
    path('view/', view_profile, name='view_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile'),
    
]

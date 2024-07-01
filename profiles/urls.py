from django.urls import path
from .views import view_profile, edit_profile, delete_profile
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('view/', view_profile, name='view_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile'),
]

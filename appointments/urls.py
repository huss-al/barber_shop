from django.urls import path
from . import views

urlpatterns = [
    path('book-now/', views.book_now, name='book_now'),
    path('book-now/login/', views.redirect_to_login, name='redirect_to_login'),
]

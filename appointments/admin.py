from django.contrib import admin
from .models import Appointment, CutType

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'barber', 'datetime', 'cut')
    search_fields = ('client__firstname', 'client__surname', 'barber__name', 'cut__name')

@admin.register(CutType)
class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')



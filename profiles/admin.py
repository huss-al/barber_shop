from django.contrib import admin
from .models import Profile, CutType

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'surname')

class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')

admin.site.register(CutType, CutTypeAdmin)

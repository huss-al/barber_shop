from django.contrib import admin
from .models import Profile, CutType, Gallery, AboutUsContent, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'surname')


class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')

admin.site.register(CutType, CutTypeAdmin)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

admin.site.register(AboutUsContent)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')



from django.contrib import admin
from .models import Profile, CutType, Gallery

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'surname')


class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')

admin.site.register(CutType, CutTypeAdmin)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

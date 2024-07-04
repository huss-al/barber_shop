from django.contrib import admin
from .models import Profile, CutType, Gallery, AboutUsContent, ContactMessage, Appointment

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


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'cut', 'barber')  # Customize this as needed
    list_filter = ('barber', 'datetime')  # Add filters
    search_fields = ('barber__name', 'cut__name') # Add search fields

    # Customize the form fields displayed in admin if needed
    fieldsets = (
        (None, {
            'fields': ('datetime', 'cut', 'barber')
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "barber":
            # Filter the queryset for the 'barber' field to only show available barbers
            kwargs["queryset"] = kwargs.get("queryset", db_field.remote_field.model.objects).filter(is_available=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


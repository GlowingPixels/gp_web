"""Admin Class of Gallery App that implements filter by date of upload"""
from django.contrib import admin
from .models import Gallery, ImageCategory


class GalleryAdmin(admin.ModelAdmin):
    """The only Main class of Gallery Admin"""
    list_display = ('label', 'date', 'category')
    list_filter = ('date', 'category')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageCategory)

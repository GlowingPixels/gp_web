"""Admin Class of Gallery App that implements filter by date of upload"""
from django.contrib import admin
from .models import Image, ImageCategory, Tag


class ImageAdmin(admin.ModelAdmin):
    """The only Main class of Gallery Admin"""
    list_display = ('label', 'date', 'category')
    list_filter = ('date', 'category')

admin.site.register(Image, ImageAdmin)
admin.site.register(ImageCategory)
admin.site.register(Tag)

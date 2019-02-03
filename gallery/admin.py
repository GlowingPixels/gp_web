"""Admin Class of Gallery App that implements filter by date of upload"""
from django.contrib import admin
from .models import Image, ImageCategory, Tag, SubCategory


class ImageAdmin(admin.ModelAdmin):

    list_display = ('label', 'date', 'category')
    list_filter = ('date', 'category')

class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent')
    list_filter = ('parent',)
    
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageCategory)
admin.site.register(Tag)
admin.site.register(SubCategory, SubCategoryAdmin)

from django.contrib import admin
from .models import Sweatshirt, Photo


@admin.register(Sweatshirt)
class SweatAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'price',)
    list_display_links = list_display


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sweatshirt')
    list_display_links = list_display
from django.contrib import admin
from .models import Sweatshirt, Photo

@admin.register(Sweatshirt)
class SweatAdmin(admin.ModelAdmin):
    list_display = ('id', 'price',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sweatshirt',)
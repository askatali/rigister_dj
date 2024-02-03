from django.contrib import admin
from product.models import Frame, Image


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'frame')

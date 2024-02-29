from rest_framework import serializers
from fashion.models import Sweatshirt, Photo


class SweatshirtListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweatshirt
        fields = ('id', 'price', 'photo',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo')


class SweatDetailSerializer(serializers.ModelSerializer):
    # photos = PhotoSerializer(many=True)

    class Meta:
        model = Sweatshirt
        fields = (
            'id', 'price', 'photo', 'brand', 'color', 'size', 'state', 'description', 'number', 'photos'
        )

from rest_framework import serializers

from product.models import Frame, Image


class FrameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ('id', 'code', 'image')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class FrameDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Frame
        fields = (
            'id', 'code', 'image', 'vendor_code', 'description',
            'width', 'height', 'aliquet', 'images'
        )

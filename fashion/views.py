from rest_framework.generics import ListAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response

from fashion.models import Sweatshirt, Photo
from fashion.serializers import SweatshirtListSerializer,SweatDetailSerializer


class SweatshirtListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SweatshirtListSerializer
    queryset = Sweatshirt.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SweatDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = SweatDetailSerializer
    queryset = Sweatshirt.objects.all()
    lookup_field = 'id'


class SweatDeleteView(DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Sweatshirt.objects.all()
    lookup_field = 'id'





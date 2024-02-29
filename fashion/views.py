from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView, DestroyAPIView,
                                     UpdateAPIView, CreateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

from .models import Sweatshirt, Photo
from .serializers import SweatshirtListSerializer, SweatDetailSerializer, PhotoSerializer


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


class SweatUpdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SweatDetailSerializer
    queryset = Sweatshirt.objects.all()
    lookup_field = 'id'


class SweatCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SweatDetailSerializer
    queryset = Sweatshirt.objects.all()


class SweatDeleteView(DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Sweatshirt.objects.all()
    lookup_field = 'id'


class PhotoCreateAPIView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        sweatshirt_id = request.data.get('sweatshirt_id')

        try:
            sweatshirt = Sweatshirt.objects.get(id=sweatshirt_id)
            request.data['sweatshirt'] = sweatshirt.id

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Sweatshirt.DoesNotExist:
            return Response({"error": f"Sweatshirt with ID {sweatshirt_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)




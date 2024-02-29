from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response

from .models import Frame, Image
from .serializers import FrameListSerializer, FrameDetailSerializer


class FrameListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FrameListSerializer
    queryset = Frame.objects.all()

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True, context={'request': request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class FrameDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = FrameDetailSerializer
    queryset = Frame.objects.all()
    lookup_field = 'id'


class FrameDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Frame.objects.all()
    lookup_field = 'id'

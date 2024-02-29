from django.urls import path

from .views import SweatshirtListView, SweatDetailView, SweatDeleteView, SweatUpdateView, SweatCreateView, PhotoCreateAPIView

urlpatterns = [
    path('sweat_list/', SweatshirtListView.as_view(), name='sweat_list'),
    path('sweat_detail/<int:id>/', SweatDetailView.as_view(), name='sweat_detail'),
    path('sweat_delete/<int:id>/', SweatDeleteView.as_view(), name='sweat_delete'),
    path('update/<int:id>/', SweatUpdateView.as_view(), name='update'),
    path('create/', SweatCreateView.as_view(), name='create'),
    path('create_photo/<int:id>/', PhotoCreateAPIView.as_view(), name='create_photo'),
]
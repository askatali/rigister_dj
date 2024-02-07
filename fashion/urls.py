from django.urls import path

from fashion.views import SweatshirtListView, SweatDetailView,SweatDeleteView

urlpatterns = [
    path('sweat_list/', SweatshirtListView.as_view(), name='sweat_list'),
    path('sweat_detail/<int:id>/', SweatDetailView.as_view(), name='sweat_detail'),
    path('sweat_delete/<int:id>/', SweatDeleteView.as_view(), name='sweat_delete')
]
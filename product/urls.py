from django.urls import path

from product.views import FrameListView, FrameDetailView, FrameDeleteView


urlpatterns = [
    path('list/', FrameListView.as_view(), name='list'),
    path('detail/<int:id>/', FrameDetailView.as_view(), name='detail'),
    path('delete/<int:id>/', FrameDeleteView.as_view(), name='delete'),
]

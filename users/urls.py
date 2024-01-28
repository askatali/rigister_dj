from django.urls import path

from users.views import (
    RegisterView,
    VerifyEmailView,
    LoginView,
    UserProfileUpdateView,
    UserProfileDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('update_profile/', UserProfileUpdateView.as_view(), name='update_profile'),
    path('profile/', UserProfileDetailView.as_view(), name='profile'),
]

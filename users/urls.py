from django.urls import path

from users.views import RegisterView, VerifyEmailView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login')
]

from django.urls import path
from .views import RegisterView, VerifyPhoneView, LoginView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verify-phone/', VerifyPhoneView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserListView.as_view()),
]

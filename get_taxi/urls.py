from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('log-in', TokenObtainPairView.as_view()),
]

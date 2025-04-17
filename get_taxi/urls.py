from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from get_taxi.views import RequestTaxiView

urlpatterns = [
    path('log-in', TokenObtainPairView.as_view()),
    path('get-taxi', RequestTaxiView.as_view()),
]

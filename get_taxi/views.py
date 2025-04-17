from get_taxi.models import Wallet, User, Trip
from rest_framework.generics import CreateAPIView
from get_taxi.serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated
import requests
import json


def get_duration_from_neshan(origin_latitude, origin_longitude, destination_latitude, destinatio_longitude):
    url = f"https://api.neshan.org/v4/direction?origin={origin_latitude},{origin_longitude}&destination={destination_latitude},{destinatio_longitude}"
    
    headers = {
        "Api-Key": "service.52712b2d2dc743ee966ceb4f14bd2d1a"
    }

    response = requests.get(url, headers= headers)

    data= response.json()


class RequestTaxiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    get_duration_from_neshan()



    def perform_create(self, serializer):
        origin_latitude = self.request.get('origin_latitude')
        origin_longitude = self.request.get('origin_longitude')
        destination_latitude = self.request.get('destination_latitude')
        destinatio_longitude = self.request.get('destinatio_longitude')

        



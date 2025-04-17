from get_taxi.models import Wallet, User, Trip
from rest_framework.generics import CreateAPIView
from get_taxi.serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated

class RequestTaxiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        duration = Trip.objects.get('duration')
        serializer.save(
            duration = duration,
            customer = self.request.user
        )


from rest_framework.serializers import ModelSerializer
from get_taxi.models import User, Wallet, Trip

class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


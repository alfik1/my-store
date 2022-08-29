from rest_framework import serializers
from vehicle_api.models import Cars

class CarSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)#read cheyan vendi mathram aahn id not for writing so read read_only=ture.
    brand=serializers.CharField()
    model=serializers.CharField()
    fuel_capacity=serializers.IntegerField()
    top_speed=serializers.IntegerField()
    mileage=serializers.IntegerField()
    price=serializers.IntegerField()
    rating=serializers.IntegerField()

class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cars
        fields="__all__"


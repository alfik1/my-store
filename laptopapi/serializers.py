from rest_framework import serializers

class LaptopSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    screen_size=serializers.IntegerField()
    cpu=serializers.CharField()
    ram=serializers.CharField()
    price=serializers.IntegerField()
    ratings=serializers.IntegerField()

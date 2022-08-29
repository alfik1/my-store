from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from laptopapi.models import Laptops
from laptopapi.serializers import LaptopSerializer


# Create your views here.

class LaptopView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Laptops.objects.all()
        if "name" in request.query_params:
            qs=qs.objects.filter(name__contains=request.query_params.get("name"))
        if "brand" in request.query_params:
            qs=qs.objects.filter(brand=request.query_params.get("brand"))
        serializer=LaptopSerializer(qs,many=True)
        return Response(data=serializer.data)
    #for creating a new object
    def post(self,request, *args,**kwargs):
        serializer=LaptopSerializer(data=request.data)
        if serializer.is_valid():
            Laptops.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class LaptopDetailView(APIView):
    def get(self,request, *args, **kwargs):
        id=kwargs.get('id')
        qs=Laptops.objects.get(id=id)
        serializer=LaptopSerializer(qs)
        return Response(data=serializer.data)
    def post(self,request, *args, **kwargs):
        id=kwargs.get('id')
        qs=Laptops.objects.get(id=id)
        serializer=LaptopSerializer(qs)
        return Response(data=serializer)

    def delete(self,request, *args, **kwargs):
        id=kwargs.get('id')
        qs=Laptops.objects.get(id=id)
        Laptops.delete(qs)
        return Response({"succesfully removed"})
    def put(self,request, *args, **kwargs):
        id=kwargs.get('id')
        qs=Laptops.objects.filter(id=id)
        serializer=LaptopSerializer(data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)



            # qs.name=serializer.validated_data.get("name")
            # qs.brand=serializer.validated_data.get("brand")
            # qs.screen_size=serializer.validated_data.get("screen_size")
            # qs.cpu=serializer.validated_data.get("cpu")
            # qs.ram=serializer.validated_data.get("ram")
            # qs.price=serializer.validated_data.get("price")
            # qs.rating=serializer.validated_data.get("rating")
            # serializer.validated_data.get(qs)

            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)







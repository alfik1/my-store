from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from vehicle_api.serializers import CarSerializer,CarsModelSerializer
from vehicle_api.models import Cars
# Create your views here.

#api/v1/vehicles/cars
class CarView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Cars.objects.all()
        if "model" in request.query_params:
            qs=qs.filter(model__contains=request.query_params.get("model"))#model__contains ennath kodthath names of models varunath ethokke aahnen nokkan aahn
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))#qs.filter kodthath already ellam loaded aahn (line12) pinne athine filter chethal mathy
        serializer=CarSerializer(qs,many=True)#many=True kodukunath ella detailsum edkunath kondaan #deserialize cheyyuna timeil many True kodthal math
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=CarSerializer(data=request.data)
        if serializer.is_valid():
            Cars.objects.create(**serializer.validated_data)#**serializer enn kodthath ella keywordsum kodukand easy methodil cheyyan vendi aahn
            return Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)

class CarDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Cars.objects.get(id=id)
        serializer=CarSerializer(qs)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Cars.objects.get(id=id)
        serializer=CarSerializer(qs)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Cars.objects.get(id=id)
        Cars.delete(qs)
        return Response({"msg:Deleted"})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Cars.objects.filter(id=id)
        serializer=CarSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)

class CarModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Cars.objects.all()
        serializer=CarsModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=CarsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()#save function actually cheyyunath creating aahn
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class CarModelDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Cars.objects.get(id=id)
        serializer=CarsModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        cars=Cars.objects.get(id=id)
        serializer=CarsModelSerializer(instance=cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
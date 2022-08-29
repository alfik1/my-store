from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from vehicle.models import bikes
# Create your views here.

class BikeView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"details":bikes})

    def post(self,request,*args,**kwargs):
        qs=request.data
        bikes.append(qs)
        return Response({"created":qs})
class BikeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=[bike for bike in bikes if bike.get("id")==id]
        return Response({"details":qs})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=request.data
        instance=[bike for bike in bikes if bike.get("id")==id].pop()
        instance.update(data)
        return Response({"update":instance})

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        data = request.data
        instance = [bike for bike in bikes if bike.get("id") == id].pop()
        instance.remove(data)
        return Response({"update": instance})
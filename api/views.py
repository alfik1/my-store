from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class MyView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({"message":"hello world"})

class GoodMorningView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({"msg":"Good morning"})

class GoodEveningView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({"msg":"Good Evening"})

class GoodNightView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({"msg":"Good Night"})

class ThankyouView(APIView):
    def get(self,request, *args, **kwargs):
        return Response({"msg":"Thank You"})

class AddView(APIView):
    def post(self,request, *args, **kwargs):
        print(request.data)#client send cheyyana value kittane request.data ennathilan kittunath
        n1=int(request.data.get("n1"))
        n2=int(request.data.get("n2"))
        res=n1+n2
        return Response({"msg":res})


class SubtractionView(APIView):
    def post(self,request, *args, **kwargs):
        n1=int(request.data.get("n1"))
        n2=int(request.data.get("n2"))
        res=n1-n2
        return Response({"msg":res})
#multiplication
class MultiplicationView(APIView):
    def post(self,request, *args, **kwargs):
        n1=int(request.data.get("n1"))
        n2=int(request.data.get("n2"))
        res=n1*n2
        return Response({"msg":res})

#cube
class CubeView(APIView):
    def post(self,request, *args, **kwargs):
        n1=int(request.data.get("n1"))
        res=n1*n1*n1
        return Response({"msg":res})
#factorial
class FactorialView(APIView):
    def post(self,request, *args, **kwargs):
        n1=int(request.data.get("n1"))
        factorial=1
        for i in range(1,n1+1):
            factorial=factorial*i
        return Response({"msg":factorial})



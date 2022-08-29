from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles
# Create your views here.

class MobilesView(APIView):

    def get(self,request,*args,**kwargs):
        all_mobiles = mobiles
        if 'display' in request.query_params:
            disp=request.query_params.get('display')
            all_mobiles=[mob for mob in all_mobiles if mob.get('display')==disp]
        # print(request.query_params)
        # disp=request.query_params.get('display')
        # print(disp)
        if 'brand' in request.query_params:
            bname=request.query_params.get('brand')
            all_mobiles=[mob for mob in all_mobiles if mob.get('brand')==bname]

        return Response({"mobiles":all_mobiles})
    def post(self,request,*args,**kwargs):
        print(request.data)
        qs=request.data
        mobiles.append(qs)
        return Response({"msg":qs})

class MobileDetailView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        return Response({"data":qs})

    def put(self, request, *args, **kwargs):
        id=kwargs.get("id")
        data=request.data
        instance=[ mobile for mobile in mobiles if mobile.get("id")==id].pop()
        instance.update(data)
        return Response({"data":instance})

    def  delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=[ mobile for mobile in mobiles if mobile.get("id")==id].pop()
        mobiles.remove(instance)
        return Response({"deleted":instance})

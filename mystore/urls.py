"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from mobile.views import MobilesView,MobileDetailView
from vehicle.views import BikeView,BikeDetailView
from vehicle_api import views as apiview      #viewsine apiviews aay kodthath mukalil ulla viewsumaay conflict vaarathe irikaan aaahn
from laptopapi import views as lapapiview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/laptops/all/',lapapiview.LaptopView.as_view()),
    path('api/v1/laptops/<int:id>',lapapiview.LaptopDetailView.as_view()),
    path('api/v1/vehicles/cars',apiview.CarView.as_view()),
    path('api/v1/vehicles/cars/<int:id>',apiview.CarDetailView.as_view()),
    path('api/v2/vehicles/cars',apiview.CarModelView.as_view()),
    path('api/v2/vehicles/<int:id>',apiview.CarModelDetailView.as_view()),
    # path('morning/', views.GoodMorningView.as_view()),
    # path("evening/",views.GoodEveningView.as_view()),
    # path("night/",views.GoodNightView.as_view()),
    # path('add/',views.AddView.as_view()),
    # path('sub/',views.SubtractionView.as_view()),
    # path('multiplication/',views.MultiplicationView.as_view()),
    # path('cube/',views.CubeView.as_view()),
    # path('fact/',views.FactorialView.as_view()),
    # path('api/v1/mobile/',MobilesView.as_view()),
    # path('api/v1/mobile/<int:id>',MobileDetailView.as_view()),
    # path('api/bikes/',BikeView.as_view()),
    # path('api/bikes/<int:id>',BikeDetailView.as_view()),

]
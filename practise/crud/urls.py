from django.urls import path
from crud.views import getallstudnets,getactivestudnets

urlpatterns = [
    path('',getallstudnets,name='get'),
    path('filter',getactivestudnets,name='getfilter'),
]


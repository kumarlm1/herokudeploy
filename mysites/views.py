from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from rest_framework.views import APIView
# Create your views here.

class Landing_Page(APIView):
    def get(self,request):
        now = datetime.datetime.now()
        json={
        'time' : "%s" % now
        }
        return JsonResponse(json)
        

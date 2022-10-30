from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from .models import  *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HNGUserViewSet(generics.ListAPIView):
    queryset = HNGUser.objects.all()
    serializer_class = HNGUserSerializer

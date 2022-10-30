from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from .models import  *
from .serializers import *

# Create your views here.
def index(request):
    get_user = HNGUser.objects.all()
    query_dict = {}
    if get_user.count() > 0:
        # get the first part
        first = get_user[0]
        query_dict['slackUsername'] = first.slackUsername
        query_dict['backend'] = first.backend
        query_dict['age'] = first.age
        query_dict['bio'] = first.bio
    
    return JsonResponse(query_dict)

class HNGUserViewSet(generics.ListAPIView):
    queryset = HNGUser.objects.all()
    serializer_class = HNGUserSerializer

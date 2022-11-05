from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  *
from django.views import View
from rest_framework import status
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utility import *

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

@method_decorator(csrf_exempt, name='dispatch')
class SendData(View):
    def post(self, request):
        query_dict = {}
        get_data = json.loads(request.body.decode("utf-8"))
        operator = get_data.get("operation_type")
        x_value = get_data.get("x")
        y_value = get_data.get("y")   
        get_result, operation = get_operation(operator, x_value, y_value)
        if get_result is None:
            query_dict["slackUsername"] = "DayBme"
            query_dict["operation_type"] = operation
            query_dict["result"] = "Incompatible types" 
            get_status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        else:
            query_dict["slackUsername"] = "DayBme"
            query_dict["operation_type"] = operation
            query_dict["result"] = get_result
            get_status = status.HTTP_202_ACCEPTED     
        return JsonResponse(query_dict)        
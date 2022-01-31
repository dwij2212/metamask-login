from tkinter import E
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import MetamaskUser
# Create your views here.
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

def home(request):
    request.user = None
    return render(request, 'index.html')

@csrf_exempt
def auth(request):

    if request.method == 'POST':
        addr = request.POST.get('addr')
        try:
            user = MetamaskUser.objects.get(address=addr)
            request.user = user.name
            response = {'status': 1, 'message': user.name} 
            return HttpResponse(json.dumps(response), content_type='application/json')

        except ObjectDoesNotExist as e:
            response = {'status': 0, 'message': "No such user!"} 
            return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        return render(request, 'auth.html', {"user": request.user})   

def err(request):
    return render(request, 'err.html') 

    
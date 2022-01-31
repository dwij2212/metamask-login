from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import MetamaskUser
# Create your views here.
from django.http import HttpResponse
import json

def home(request):
    request.user = None
    return render(request, 'index.html')

@csrf_exempt
def auth(request):

    if request.method == 'POST':
        addr = request.POST.get('addr')
        try:
            user = MetamaskUser.objects.all()
            print(user)
            request.user = user
            response = {'status': 1, 'message': user} 
            return HttpResponse(json.dumps(response), content_type='application/json')
        except:
            print("User not found")
            response = {'status': 0, 'message': "No such user!"} 
            return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        return render(request, 'auth.html', {"user": request.user})   

def err(request):
    return render(request, 'err.html') 

    
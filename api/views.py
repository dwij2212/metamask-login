from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import MetamaskUser
# Create your views here.

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def auth(request):

    if request.method == 'POST':
        print("addr", request.POST.get('addr'))
        addr = request.POST.get('addr')

        try:
            user = MetamaskUser.objects.get(address=str(addr))
            request.user = user
            return render(request, 'auth.html', {'user': user.name})
        except:
            return render(request, 'auth.html', {"error": "User not found"})

    else:
        return render(request, 'auth.html', {"user": request.user})    

    
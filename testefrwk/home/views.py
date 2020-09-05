from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    if request.user.is_authenticated:
        return redirect('albuns/lista')
    else:
        return redirect('login/')
    
   #  return render(request, 'home.html')
    


def my_logout(request):
    logout(request)
    return redirect('home')

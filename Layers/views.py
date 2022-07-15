from django.shortcuts import render, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def login(request):



    if request.method == 'POST':

        print('request method is post')
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
        return HttpResponseRedirect(reverse('dashboard_view'))

    else:
        return render(request, 'layers/login.html')



def logout(request):
        # logout(request)
        return HttpResponseRedirect(reverse('login'))
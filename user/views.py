from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate, logout

def sign_form(request):
    if request.method == 'GET':
        return render(request,'user/login_form.html')
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return redirect('categorylist')
def sign_out(request):
    logout(request)
    return redirect('login_form')            

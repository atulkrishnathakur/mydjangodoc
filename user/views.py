from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
import random

def signup_form(request):
    if request.method == 'GET':
        return render(request,'user/signup_form.html')
def signup_save(request):

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email'];
        username = random.randrange(9999, 9999999)
        errors = {}
        if not first_name:
            errors['first_name'] = 'First Name field is required'
        if not last_name:
            errors['last_name'] = 'Last name field is required'
        if not email:
            errors['email'] = 'Email field is required' 
        if not password:
            errors['password'] = 'Password field is required'
        elif len(password) < 8:
            errors['password'] = 'Enter atleast 8 character in password'  
                
        context = {
            'errors': errors,
        }
        if errors:        
            return render(request,'user/signup_form.html',context)   
        password = make_password(request.POST['password'])            
        userobj = User(username=username,email=email,first_name=first_name,last_name=last_name,password=password,is_active=1,is_staff=1)
        userobj.save()
        return redirect('login_form')
        
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

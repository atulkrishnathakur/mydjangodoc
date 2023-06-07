from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')
    
def home_temp(request):
    return render(request,'productmanagement/home.html')
    
def about_temp(request):
    return render(request,'productmanagement/about.html')    
    
mybooks = [
{
'math_type': 'Arithmetic math',
'author': 'Atul',
'content': 'All chapters',
'published_at': '01-may-2023'
},
{
'math_type': 'Arithmetic math',
'author': 'Atul',
'content': 'All chapters',
'published_at': '01-may-2023'
}
] 
    
def show_data(request):
    context = {
        'books': mybooks
    }

    return render(request,'productmanagement/showdata.html',context)
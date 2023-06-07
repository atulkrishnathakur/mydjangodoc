from django.shortcuts import render
from django.http import HttpResponse
from productmanagement.models.categories import Category

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
    
def create_category(request):
    return render(request,'productmanagement/create_category.html')
    
def save_category(request):
    if request.method == "POST":
        category_name = request.POST['category_name']
        catobj = Category(category_name=category_name)
        catobj.save()
        # print(category_name)
        #return HttpResponse(category_name)
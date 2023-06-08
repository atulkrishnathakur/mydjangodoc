from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
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
    try:
        if request.method == "POST":
            category_name = request.POST['category_name']
            category_code = request.POST['category_code']
            description = request.POST['description']
            longdescription = request.POST['long_description']
            short_description = request.POST['short_description']
            catobj = Category(category_name=category_name,category_code=category_code,description=description,lg_description=longdescription,sh_description=short_description)
            catobj.save()
            #sh_description: defined in model
            #lg_description: defined in model
        
            # print(category_name)
            #return HttpResponse(category_name)
    except Exception as e:
        print(e)
        
def category_list(request):
    try:
        if request.method == "GET":
            categoryall = Category.objects.all()
            template = loader.get_template("productmanagement/category_list.html")
            context = {
                'categories': categoryall,
            }
            return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
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
            image = request.FILES['catimage']
            catobj = Category(category_name=category_name,category_code=category_code,description=description,lg_description=longdescription,sh_description=short_description)
            catobj.save()
            return redirect('categorylist')
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
        
def category_edit(request,id):
    try:
        if request.method == "GET":
            category = Category.objects.get(cat_id = id)
            template = loader.get_template("productmanagement/category_edit.html")
            context = {
                'category': category,
            }
            return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)
        
def category_update(request):
    try:
        if request.method == "POST":
            category_id = request.POST['category_id']
            category_name = request.POST['category_name']
            category_code = request.POST['category_code']
            description = request.POST['description']
            longdescription = request.POST['long_description']
            short_description = request.POST['short_description']
            category = Category.objects.get(cat_id = category_id)
            category.category_name = category_name
            category.category_code = category_code
            category.description = description
            category.lg_description = longdescription
            category.sh_description = short_description
            category.save()
            return redirect('categorylist')
    except Exception as e:
        print(e)
     
def category_delete(request,id):
    try:
        if request.method == "GET":
            category = Category.objects.get(cat_id = id)
            category.delete()
            return redirect('categorylist')
    except Exception as e:
        print(e)
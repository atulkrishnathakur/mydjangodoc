from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from productmanagement.models.categories import Category
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.conf import settings
#from mydjangodoc import settings_production
from productmanagement.constants import MAXIMUM_RETRIES, DEFAULT_USERNAME, VALID_STATUSES
import logging
logger = logging.getLogger(__name__)

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
            myimage = request.FILES['catimage']
            imagename = myimage.name
            imgmediapath = "category/"+imagename
            fs = FileSystemStorage()
            imagefile = fs.save(imgmediapath, myimage)
            catobj = Category(category_name=category_name,category_code=category_code,description=description,lg_description=longdescription,sh_description=short_description,image=imagefile)
            catobj.save()
            return redirect('categorylist')
    except Exception as e:
        print(e)
        
@login_required        
def category_list(request):
    print(HttpResponse(request))
    try:
        if request.method == "GET":
            custom_setting_value = settings.MY_CUSTOM_SETTING
            max_retries = MAXIMUM_RETRIES
            default_username = DEFAULT_USERNAME
            valid_statuses = VALID_STATUSES
            categoryall = Category.objects.all()
            template = loader.get_template("productmanagement/category_list.html")
            context = {
                'categories': categoryall,
                'custom_setting_value': custom_setting_value,
                'max_retries': max_retries,
                'default_username': default_username,
                'valid_statuses': valid_statuses
            }
            return HttpResponse(template.render(context, request))
        else:
            return redirect('login_form')        
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
        
def testLog(request):
    try:
        logger.debug("This is debug log")
        logger.info("This is info log")
        logger.warning("This is warning log")
        logger.error("This is error log")
        logger.critical("This is critical log")
        context = {
        }
        return HttpResponse(context)
    except Exception as e:
        print(e)
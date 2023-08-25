from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from productmanagement.models.categories import Category
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from productmanagement.models.product import Product

import logging

logger = logging.getLogger(__name__)

def  create_product(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    template = loader.get_template("productmanagement/create_product.html")
    return HttpResponse(template.render(context,request));
    
def get_category_ajax(request):
    try:
        if request.method == 'POST':
            id = request.POST['cat_id'];
            category = Category.objects.get(cat_id = id)
            catcode = category.category_code
            #context = {"categoryObj": categoryObj}
            context = {
                "catcode":catcode
            }
            return JsonResponse(context)
    except Exception as e:
        logger.debug(e)
        
def save_product(request):
    try:
        if request.method == 'POST':
            catid = request.POST['category_id']
            productname = request.POST['product_name'];
            productcode = request.POST['product_code'];
            #myimage = request.FILES['productimage']
            #imagename = myimage.name
            #imgmediapath = "product/"+imagename
            #fs = FileSystemStorage()
            #imagefile = fs.save(imgmediapath, myimage)
            #prodobj = Product(product_name="dd",cat_id=2,image="ddd.png")
            #prodobj.save()
    except Exception as e:
        print(e)
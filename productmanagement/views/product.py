from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from productmanagement.models.categories import Category
from productmanagement.models.product import Product
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage


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

def saveproduct(request):
    try:
        if request.method == "POST":
            catid = request.POST['category_id']
            product_name = request.POST['product_name']
            category = Category.objects.get(cat_id = catid)
            prodobj = Product.objects.create(product_name=product_name,image="abc.png",cat_id=category)
            #prodobj.save()
            return redirect('categorylist')
    except Exception as e:
        print(e)
        
        
def product_list(request):
    try:    
        if request.method == "GET":
            productAll = Product.objects.all() # left ourter join means left join
            #print(str(productAll)) 
            #print(str(productAll.query))
            cat  =  productAll[3].cat_id
            template = loader.get_template("productmanagement/product_list.html")
            context = {
                'productAll':productAll
            }
            return HttpResponse(template.render(context, request))
        else:
            return         
    except Exception as e:
        print(e)
from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Category,Product
# Create your views here.
import random
def index(request):
    productlist1 = Product.objects.filter(category = 1)
    productlist2 = Product.objects.filter(category = 2)
    productlist3 = Product.objects.filter(category = 3)
    productlist4 = Product.objects.filter(category = 4)

    productlist1 = productlist1[:4]
    productlist2 = productlist2[:4]
    productlist3 = productlist3[:4]
    productlist4 = productlist4[:4]

    context = {
        #"categories":category,
        'products1':productlist1,
        'Products2':productlist2,
        'Products3':productlist3,
        'Products4':productlist4,

    }
    return render(request,'index.html',context)


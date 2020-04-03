from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Category,Product,ProductImages
from . import models
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .forms import AddProductsPost,AddImageForm

# Create your views here.



def productlist(request,category_slug=None):
    category = None
    productlist = models.Product.objects.all()
    categorylist = models.Category.objects.annotate(total_products = Count('product'))
    if category_slug:
        category = get_object_or_404(models.Category,slug=category_slug)
        productlist = productlist.filter(category=category)


    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains = search_query)|
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
            Q(brand__brand_name__icontains=search_query)|
            Q(category__category_name__icontains=search_query)

        )


    paginator = Paginator(productlist,10)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {
        'product_list': productlist,
        'category_list':categorylist,
        'category':category
    }
    templates = 'product_list.html'

    return render(request,templates,context)



def productdetail(request,slug,id):
    try:
        product_details = get_object_or_404(Product,slug=slug)
        productimages = models.ProductImages.objects.filter(product_slug=product_details)
    except:
        product_details = get_object_or_404(Product,id=id)
        productimages = models.ProductImages.objects.filter(product_id=product_details)
    context = {
        "product_details":product_details,
        'productimages':productimages,
    }
    templates = 'product_details.html'
    return render(request,templates,context)


def add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddProductsPost(request.POST or None ,request.FILES or None)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.owner = request.user
                new_form.save()
                print(new_form.id)
                return redirect('products:product_detail',slug=new_form.slug,id=new_form.id)
        else:
            form = AddProductsPost()
        context = {
            'form':form

        }
        return render(request,'add_product.html',context)
    else:
        return redirect('accounts:login')


def update_product(request,slug=None,id=None):
    if request.user.is_authenticated:
        try:
            product = get_object_or_404(Product,slug=slug)
        except:
            product = get_object_or_404(Product,id=id)
        if request.method == 'POST':
            form = AddProductsPost(request.POST or None,request.FILES or None,instance=product)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.owner = request.user
                new_form.save()
                print(new_form.slug,new_form.id)
            return redirect('products:product_detail',slug=new_form.slug,id=new_form.id)
        else:
            form = AddProductsPost(instance=product)
        context = {
            'form':form,
        }
        return render(request,'update_product.html',context)
    else:
        return redirect('accounts:login')


def add_image_product(request,id,slug):
    if request.user.is_authenticated:
        try:
            product = get_object_or_404(Product, slug=slug)
        except:
            product = get_object_or_404(Product, id=id)
        if request.method == 'POST':
            form = AddImageForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.product = product
                new_form.save()
                return redirect('products:product_list')
        else:
            form = AddImageForm()
            image_products = ProductImages.objects.all().filter(product=id)
        context = {
            'form': form,
            'image_products':image_products,
        }


        return render(request, 'add_image.html', context)
    else:
        return redirect('accounts:login')



def delete_product(request,slug=None,id=None):
    if request.user.is_authenticated:
        try:
            product = get_object_or_404(Product, slug=slug)
        except:
            product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect('accounts:dashboard')
    return redirect('/')
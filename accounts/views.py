from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

from accounts.models import User_Profile
from .forms import SignUpForm, ProfileForm, EditUserDate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from product.models import Product



# Create your views here.

def login_view(request):
    if request.method =='POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<center><h1>Your User Name Or Password Is not avilapel</h1></center>')
    else:
        return render(request,'registration/login.html',{})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:add_profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_profile(request,user=None):
    if request.method == "POST":
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.phone = form.cleaned_data.get('phone')
            new_form.address = form.cleaned_data.get('address')
            new_form.user_img = form.cleaned_data.get('user_img')
            new_form.save()
            return redirect('/')
    else:
        form = ProfileForm()
    context = {
        'form':form
    }
    return render(request,'registration/create_profile.html',context)




def dashboard(request):
    user_products = Product.objects.all().filter(owner_id=request.user.id)
    user_profile = User_Profile.objects.all().get(user=request.user.id)
    context = {
        'products':user_products,
        'user_profile':user_profile
    }
    return render(request,'dashboard.html',context)




def edit_user_profile(request):
    pass
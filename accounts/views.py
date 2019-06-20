from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
from product.models import Product


def home(request):
    products = Product.objects
    return render(request, 'product/home.html',{'products':products})


def signup(request):
    if request.method == 'POST' and request.POST['username']!= ''  and request.POST['password1'] != '' and request.POST['password2']  != '' and request.POST['password1'] == request.POST['password2'] :
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=(request.POST['username']))
                return render(request, 'product/signup.html', {'error': 'username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')

    else:
            return render(request, 'product/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request,'product/login.html',{'error':'invalid user or password'})
    else:
        return render(request, 'product/login.html')



def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')



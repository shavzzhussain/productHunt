from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product


def home(request):
    return render(request, 'product/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and \
                request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.vote_count = 1
            product.date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/product/' + str(product.id)) #to show the product via id
        else:
            return render(request, 'product/product_create.html', {'error': 'All fields must be filled'})
    else:
        return render(request, 'product/product_create.html')


def detail(request, product_id):
    #to show the product o 404 error
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})

@login_required()
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.vote_count += 1
        product.save()
        return redirect('/product/' + str(product.id))



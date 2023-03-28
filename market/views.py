from django.shortcuts import render, HttpResponse, redirect
from market.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginUserForm , ProductForm
from django.utils.text import slugify

from products.models import Products

# Create your views here.


def home(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'market/index.html', context)


def become_vendor(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('vendor-admin')

    else:
        form = CreateUserForm()

    return render(request, 'market/register_vendor.html', {'form': form})


@login_required()
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'market/vendor-admin.html', {'vendor': vendor, 'products': products })


@login_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor-admin')
    else:
        form = ProductForm()

    return render(request, 'market/add_product.html', {'form': form})


def login_user(request):

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
    else:
        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'market/login.html', context)


def products(request):
    newest_products = Products.objects.all()[0:8]
    return render(request, 'market/products.html', {'newest_products': newest_products})


def dashboard(request):
    context = {}
    return render(request, 'market/dashboard.html', context)


def gacio(request):
    context = {}
    return render(request, 'market/gacio.html', context)


def kingero(request):
    context = {}
    return render(request, 'market/kingero.html', context)


def wangige(request):
    context = {}
    return render(request, 'market/wangige.html', context)


def mjanja(request):
    context = {}
    return render(request, 'market/mjanja.html', context)


def cart(request):
    context = {}
    return render(request, 'market/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'market/checkout.html', context)


def liqor(request):
    context = {}
    return render(request, 'market/liqor.html', context)


def register_user(request):
    context = {}
    return render(request, 'market/reg_user.html', context)


def register_vendor(request):
    context = {}
    return render(request, 'market/reg_vendor.html', context)




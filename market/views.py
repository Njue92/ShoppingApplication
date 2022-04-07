from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    context = {}
    return render(request,'market/index.html', context)


def products(request):
    context = {}
    return render(request,'market/products.html', context)


def gacio(request):
    context = {}
    return render(request,'market/gacio.html', context)


def kingero(request):
    context = {}
    return render(request,'market/kingero.html', context)


def wangige(request):
    context = {}
    return render(request,'market/wangige.html', context)


def mjanja(request):
    context = {}
    return render(request,'market/mjanja.html', context)


def cart(request):
    context = {}
    return render(request,'market/cart.html', context)


def checkout(request):
    context = {}
    return render(request,'market/checkout.html', context)


def liqor(request):
    context = {}
    return render(request,'market/liqor.html', context)
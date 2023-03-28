from django.shortcuts import render, get_object_or_404
import random
from .models import Category, Products

# Create your views here.


def product(request, category_slug, product_slug):
    product = get_object_or_404(Products, category_slug= category_slug, slug= product_slug)

    similar_products = list[product.category.products.exclude(id=product.id)]

    if len(similar_products)>=4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'products/product_item.html', {'product': product, 'similar_products': similar_products})

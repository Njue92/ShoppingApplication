from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('products/', views.products, name='product-page'),
    path('kingero/', views.kingero, name='kingero'),
    path('wangige/', views.wangige, name='wangige'),
    path('gacio/', views.gacio, name='gacio'),
    path('mjanja/', views.mjanja, name='mjanja'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.cart, name='checkout-page'),
    path('liqor/', views.liqor, name='liqor'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('products/', views.products, name='product-page'),
    path('kingero/', views.kingero, name='kingero'),
    path('wangige/', views.wangige, name='wangige'),
    path('gacio/', views.gacio, name='gacio'),
    path('mjanja/', views.mjanja, name='mjanja'),
    path('cart/', views.cart, name='cart-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('liqor/', views.liqor, name='liqor'),
    path('vendor/', views.become_vendor, name='become_vendor'),
    path('register_user/', views.register_user, name='reg_user'),
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('register_vendor/', views.register_vendor, name='reg_vendor'),
    path('vendor-admin', views.vendor_admin, name='vendor-admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login_user/', auth_views.LoginView.as_view(template_name='market/login.html'), name='login'),
    path('add-product/', views.add_product, name='add_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

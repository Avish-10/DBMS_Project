"""
URL configuration for dbms1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in,name='log_in'),
    path('sign_up/', views.sign_up,name='sign_up'),
    path('home/', views.home,name='home'),
    path('log_out/', views.log_out,name='log_out'),
    path('users/', views.users,name='users'),
    path('suppliers/', views.suppliers,name='suppliers'),
    path('inventory/', views.inventory,name='inventory'),
    path('medsuppliers/', views.medsuppliers,name='medsuppliers'),
    path('orders/', views.orders,name='orders'),
    path('check_availability/', views.check_availability,name='check_availability'),
]

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from products.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name="all_products"),
    path('products/', products_view, name="all_products"),
    path('detail/<int:product_id>', product_detail, name="product_detail"),
    path('delete-product/<int:product_id>', delete_product, name="delete_product"),
    # path('search/', search_product, name="search_product"),
    path('output/', show_output, name="show_output")
]
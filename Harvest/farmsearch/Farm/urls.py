from django.contrib import admin
from django.urls import path
from productsearch.api.views import ProductList
from productsearch.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductList.as_view()),
    path('products/', product_list),
]

from django.urls import path , include
from . import views


app_name = 'product'

urlpatterns = [
    path('', views.IndexListView.as_view(), name = 'index') ,
    

    path('products/' , views.ProductListView.as_view(), name ='productlist'),


    # path('products/details/<int:pk>/' , views.ProductDetails.as_view(), name ='productdetails'),


    path('products/details/<slug:slug>/' , views.ProductDetails.as_view(), name ='productdetails'),

    path('products/search/' , views.SearchView.as_view() , name = 'product_search'),


]
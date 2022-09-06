from django.urls import path 
from . import views


app_name = 'order'

urlpatterns = [

    path('item/<slug:slug>/add/' , views.Add_To_Cart.as_view() , name = 'add_to_cart'),


    path('items/cart/' ,views.CartView.as_view() , name ='cart') ,


    path('item/cart/update/' ,views.Update_Cart.as_view() , name ='update') ,


    path('item/cart/delete/<slug:slug>/' ,views.Delete_Cart.as_view() , name ='delete') ,

] 
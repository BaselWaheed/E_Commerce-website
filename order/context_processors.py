from .models import Order 



def cart(request):
    
    if request.user.is_authenticated:
        try :
            order = Order.objects.get(is_finished=False , customer=request.user)
            data = {'items': order.cart_set.all().order_by('id') ,
            "total_price" : order.get_total_price() ,
            "quantity" :  order.cart_set.all().count(),
            "message" : '',
            }
        except :
            data = {"message" : "No item in Cart "}
    else :
        data = {"message" : "No item in Cart "}
        
    return data 




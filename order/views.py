from django.shortcuts import render , HttpResponse , HttpResponseRedirect , redirect ,get_object_or_404
from product.models import Category, Product
from .models import  Order , Cart
from django.views import View
# Create your views here.



class CartView(View):
      def get(self, request , *args , **kwargs):

        products = Product.objects.all()
        context = {
            'products' :products ,
        }
        return render(request, 'order/shop-shopping-cart.html' , context)





class Add_To_Cart(View):

    def get(self, request , *args , **kwargs):

        if request.user.is_authenticated:
            product = get_object_or_404(Product ,pro_slug=kwargs['slug'])
            quantity = int(request.GET['quantity']) 
            if 'size' in request.GET : 
                size = request.GET['size']
            else :
                size = None
            old_order , created = Order.objects.get_or_create(customer=request.user , is_finished=False)
            if product in old_order.order_contain.all():
                old_product = Cart.objects.get(order=old_order,product=product)
                if quantity > 1 :
                    old_product.quantity = quantity
                else :
                    old_product.quantity += 1
                old_product.size = size
                old_product.save()
            else :
                new_dish = Cart.objects.create(product=product , order=old_order , quantity= quantity ,size=size  ,in_cart=True)

        else :
            return redirect('accounts:login')

        return HttpResponseRedirect(redirect_to='/products/')
        




class Update_Cart(View):
    def post(self, request , *args , **kwargs):
        if request.user.is_authenticated:
            cart = get_object_or_404(Cart ,id=request.POST['cart_id'] ,in_cart=True)
            if 'quantity'  in request.POST :
                cart.quantity = request.POST['quantity']
            elif 'size'  in request.POST :
                cart.size = request.POST['size']
                print( 'baselwaheed',request.POST['size'])
            cart.save()
        return HttpResponseRedirect(redirect_to='/order/items/cart/')



   

class Delete_Cart(View):
    def get(self, request , *args , **kwargs):
        if request.user.is_authenticated:
            cart = get_object_or_404(Cart ,slug=kwargs['slug'] ,in_cart=True)
            cart.delete()
        return HttpResponseRedirect(redirect_to='/order/items/cart/')
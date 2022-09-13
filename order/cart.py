# from decimal import Decimal

# from product.models import Product


# class Basket():

#     def __init__(self, request):
#         self.session = request.session
#         basket = self.session.get('skey')
#         if 'skey' not in request.session:
#             basket = self.session['skey'] = {}
#         self.basket = basket

#     def add(self, product, qty):
#         """
#         Adding and updating the users basket session data
#         """
#         product_id = str(product.id)

#         if product_id in self.basket:
#             self.basket[product_id]['qty'] = qty
#         else:
#             self.basket[product_id] = {'price': str(product.price), 'qty': qty}

#         self.save()

#     def __iter__(self):
#         """
#         Collect the product_id in the session data to query the database
#         and return products
#         """
#         product_ids = self.basket.keys()
#         products = Product.products.filter(id__in=product_ids)
#         basket = self.basket.copy()

#         for product in products:
#             basket[str(product.id)]['product'] = product

#         for item in basket.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['qty']
#             yield item

#     def __len__(self):
#         """
#         Get the basket data and count the qty of items
#         """
#         return sum(item['qty'] for item in self.basket.values())

#     def update(self, product, qty):
#         """
#         Update values in session data
#         """
#         product_id = str(product)
#         if product_id in self.basket:
#             self.basket[product_id]['qty'] = qty
#         self.save()

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

#     def delete(self, product):
#         """
#         Delete item from session data
#         """
#         product_id = str(product)

#         if product_id in self.basket:
#             del self.basket[product_id]
#             print(product_id)
#             self.save()

#     def save(self):
#         self.session.modified = True


class Cart:
    """
    class cart to 
    
    """


    def __init__(self , request):
        self.session = request.session
        try :
            cart = self.session['cart']
        except:
            cart =self.session['cart'] = {}
        self.cart = cart
        

    def add_to_cart(self,product , quantity , size=None) :
        product_id = str(product.id)
        if  product_id  not in self.cart :
            self.cart[product_id] = {"slug":product.pro_slug,"name": product.pro_name,"quantity" : quantity , "price" : product.pro_total_price  , "size" :size  , 'image':product.pro_image}
        else :
            self.cart[product_id]["quantity"] += 1 
        self.save()
        return self.cart

    def update_cart(self , product  , quantity=None , size=None):
        product_id = str(product.id)
        if quantity != None :
            print(self.cart[product_id]["quantity"] )
            self.cart[product_id]["quantity"] = quantity
        if size != None :
            self.cart[product_id]["size"] = size
        self.save()
        return self.cart

    def delete_item(self , product):
        product_id = str(product.id)
        self.cart.pop(product_id)
        self.save()
        return self.cart


    def get_total_price(self):
        return sum( item['quantity']* item['price']  for item in self.cart.values())


    def __len__(self):
        return len(self.cart)


    def save(self ):
        self.session.modified = True


    def __str__(self):
        return str(self.cart)
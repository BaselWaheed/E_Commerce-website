from django.db import models
from accounts.models import CustomUser
from product.models import Product
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, verbose_name=_("customer"), on_delete=models.PROTECT)
    order_date = models.DateTimeField(_("Time"), auto_now_add=True)
    order_contain = models.ManyToManyField(Product, through='Cart')
    is_finished = models.BooleanField(default= False)
    total_price =  models.FloatField(default= 0 , null = True , blank = True)


    # def get_total_price(self):
    #     return sum([item.get_price for item in self.order_contain.all()])

    def get_total_price(self):
        order_item = self.cart_set.all()
        return sum([item.get_price for item in order_item])

    def __str__(self):
        return str(self.id)
    




class Cart(models.Model):
    slug = models.SlugField(null=True , blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE )
    size= models.CharField(_("size"), max_length=6 , null=True ,blank=True)
    quantity = models.IntegerField(null= True , blank=True)
    in_cart = models.BooleanField(default= False)

    @property
    def get_price(self):
        total = self.quantity * self.product.pro_total_price
        return total 

    def save(self,*args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.product.pro_name)
        super(Cart, self).save(*args , **kwargs)

 
    def __str__(self):
        return self.product.pro_name


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(CustomUser, verbose_name=_("customer"), on_delete=models.PROTECT)
#     order = models.ForeignKey(Order, verbose_name=_("order id"), on_delete=models.PROTECT)
#     address_1 = models.CharField(_("address 1"), max_length=150)
#     address_2 =  models.CharField(_("address 2"), max_length=150)
#     city = models.CharField(max_length=60)
#     post_code = models.CharField(_("post code "), max_length=150)
#     state = models.CharField(_("state "), max_length=150)
#     country = models.CharField(_("country "), max_length=150)

#     def __str__(self):
#         return self.address_1
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse

class Category(MPTTModel):
    cat_name = models.CharField(_("category name "), max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return self.cat_name

    class MPTTMeta:
        order_insertion_by = ['cat_name']



class ShoesSize(models.Model):
    s_size = models.IntegerField(_("size"))
    def __str__(self):
        return str(self.s_size)

class Size(models.Model):
    s_size = models.CharField(_("size"), max_length=50)
    
    def __str__(self):
        return self.s_size



class Product(models.Model):
    status =(
        ('available','available'),
        ('unavailable','unavailable'),

    )
    pro_name =models.CharField(_("name"), max_length=50)
    pro_category = models.ForeignKey(Category, verbose_name=_("category name"), on_delete=models.CASCADE)
    pro_size = models.ManyToManyField(Size, verbose_name=_("size") ,related_name='product_size', through="ProductSize")
    pro_price = models.IntegerField(_("price"))
    pro_status = models.CharField(_("status"), max_length=50 , choices=status)
    pro_discount = models.IntegerField(_("discount"), null=True , blank=True)
    pro_total_price = models.IntegerField(_("total price"), null=True , blank=True)
    pro_description = models.TextField(_("description"))
    pro_favourite = models.ManyToManyField(CustomUser, verbose_name=_("favourite") , through='FavouriteProduct')
    pro_added = models.DateField(_("added time"), auto_now=True, auto_now_add=False)
    pro_is_active = models.BooleanField(_("is active"), default=False)
    pro_image = models.URLField(_("image"), max_length=500 , null=True , blank=True)
    pro_slug = models.SlugField(null=True , blank=True)


    def save(self,*args , **kwargs):
        if not self.pro_slug:
            self.pro_slug = slugify(self.pro_name)
        super(Product ,  self).save(*args , **kwargs)

    def __str__(self):
        return self.pro_name
    


    def get_absolute_url(self):
        return reverse('product:productdetails', kwargs={"slug": self.pro_slug})

    
    
class Image(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    im_photo = models.ImageField(_("image"), upload_to='image', max_length=None , null=True , blank=True)
    im_url = models.URLField(_("url"), max_length=500)
    def __str__(self):
        return self.product.pro_name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("title"), on_delete=models.CASCADE)
    cl_size = models.ForeignKey(Size, verbose_name=_("size"), on_delete=models.CASCADE, null=True , blank=True)
    sh_size = models.ForeignKey(ShoesSize , verbose_name="size" , on_delete=models.CASCADE, null=True , blank=True)
    color = models.CharField(_("color"), max_length=50 , null=True , blank=True)
    count = models.PositiveIntegerField(_("quantity"),default=1)

    def __str__(self):
        return self.product.pro_name


class FavouriteProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

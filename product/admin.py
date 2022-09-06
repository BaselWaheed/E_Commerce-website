from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Category, Product, ShoesSize , Size , ProductSize ,Image 
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "cat_name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'pro_category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'pro_category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'




class ProductSizeAdminInline(TabularInline):
    extra = 1
    model = ProductSize


class ImageAdminInline(TabularInline):
    extra = 1
    model = Image


class ProductAdmin(admin.ModelAdmin):
    # add_form = ProductForm
    # form = ProductForm
    inlines = (ImageAdminInline,ProductSizeAdminInline,)
    list_display = ['pro_name','pro_category','pro_price','pro_total_price']

admin.site.register(Product,ProductAdmin)



class ProductSizeAdmin(admin.ModelAdmin):
    
    list_display = ['product','cl_size','sh_size','count']


admin.site.register(ProductSize,ProductSizeAdmin)





admin.site.register([Size ,Image , ShoesSize])

admin.site.register(Category ,CategoryAdmin )
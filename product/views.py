from django.shortcuts import render , get_object_or_404
from django.views import View
from django.views.generic import ListView ,DetailView
from .models import Product , Category, ProductSize
from product.search import lookup


class IndexListView(View):
      def get(self, request):
        products = Product.objects.all().order_by('-id')[:5]
        sale_products = Product.objects.filter(pro_discount__isnull=False).order_by('-id')[:3]
        category = Category.objects.all() 
        context = {
            'sale_products':sale_products,
            'products': products,
            'category' : category ,
            'color':'red',
        }
        return render(request, 'product/shop-index.html' , context)

            
class ProductListView(ListView):
    model = Product
    template_name = "product/shop-product-list.html"
    paginate_by = 20
    queryset =  Product.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
        
    def get_context_object_name(self, object_list):
        return 'products'





class ProductDetails(DetailView):
    model = Product
    template_name = 'product/shop-item.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(pro_slug=self.kwargs.get("slug"))

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetails, self).get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     return context
        
    def get_context_object_name(self, object_list):
        return 'product'




class SearchView(View):
      def get(self, request , *args , **kwargs):

        query = request.GET
        q = query.get('q')
        

        context = {

        }
        if q is not None :
            results = lookup(query=q )
            context['results'] = results
            context['query'] = q
        return render(request, 'product/shop-search-result.html' , context)



username = 'elastic'

password = 'XbpNdt0b4RpraQnIrV8nqngK'
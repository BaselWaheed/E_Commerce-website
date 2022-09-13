from django.conf.urls import  include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.urls import path
from django.views.i18n import JavaScriptCatalog 

urlpatterns = [
    # path('selectlanguage' , ),
    path('i18n/', include('django.conf.urls.i18n')),
] 


urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(('accounts/') , include('accounts.urls') ),
    path('' , include('product.urls') ),
    path(_('order/') , include('order.urls') ),
    prefix_default_language=False,

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler404 = 'accounts.views.error_404_view'

handler500 = 'accounts.views.error_500_view'
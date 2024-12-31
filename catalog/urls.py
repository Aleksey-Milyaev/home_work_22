from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]

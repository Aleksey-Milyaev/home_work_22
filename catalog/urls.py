from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ContactTemplateView, ProductListView, ProductDetailView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),

]

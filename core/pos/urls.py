from django.urls import path

from core.pos.views.category.views import *
from core.pos.views.client.views import *
from core.pos.views.company.views import CompanyUpdateView
from core.pos.views.dashboard.views import *
from core.pos.views.product.views import *
from core.pos.views.purchase.views import *
from core.pos.views.purchasePaid.views import *
from core.pos.views.sale.views import *
from core.pos.views.salePaid.views import *
from core.pos.views.supplier.views import *
from core.pos.views.tarjeta.views import *

urlpatterns = [
    # dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # category
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # client
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # supplier
    path('supplier/', SupplierListView.as_view(), name='supplier_list'),
    path('supplier/add/', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),
    # product
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # sale
    path('sale/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    # purchase
    path('purchase/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/add/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase/delete/<int:pk>/', PurchaseDeleteView.as_view(), name='purchase_delete'),
    path('purchase/update/<int:pk>/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase/invoice/pdf/<int:pk>/', PurchaseInvoicePdfView.as_view(), name='purchase_invoice_pdf'),
    # company
    path('company/update/', CompanyUpdateView.as_view(), name='company_update'),
    # tarjeta
    path('tarjeta/list/', TarjetaListView.as_view(), name='tarjeta_list'),
    path('tarjeta/add/', TarjetaCreateView.as_view(), name='tarjeta_create'),
    path('tarjeta/update/<int:pk>/', TarjetaUpdateView.as_view(), name='tarjeta_update'),
    path('tarjeta/delete/<int:pk>/', TarjetaDeleteView.as_view(), name='tarjeta_delete'),
    # Pagos Ventas
    path('salePaid/list/', SalePaidListView.as_view(), name='salePaid_list'),
    path('salePaid/add/', SalePaidCreateView.as_view(), name='salePaid_create'),
    path('salePaid/update/<int:pk>/', SalePaidUpdateView.as_view(), name='salePaid_update'),
    path('salePaid/delete/<int:pk>/', SalePaidDeleteView.as_view(), name='salePaid_delete'),
    # Pagos Compras
    path('purchasePaid/list/', PurchasePaidListView.as_view(), name='purchasePaid_list'),
    path('purchasePaid/add/', PurchasePaidCreateView.as_view(), name='purchasePaid_create'),
    path('purchasePaid/update/<int:pk>/', PurchasePaidUpdateView.as_view(), name='purchasePaid_update'),
    path('purchasePaid/delete/<int:pk>/', PurchasePaidDeleteView.as_view(), name='purchasePaid_delete'),
]

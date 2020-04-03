from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('',views.productlist,name='product_list'),
    path('add_product/', views.add_product, name='add_pro'),
    path('update_product/<str:slug>/<int:id>/',views.update_product, name='update_product'),
    path('add_product_image/<str:slug>/<int:id>/', views.add_image_product, name='add_product_image'),
    path('<str:category_slug>/',views.productlist,name = 'product_list_category'),
    path('details/<str:slug>/<int:id>/',views.productdetail,name = 'product_detail'),
    path('delete/<str:slug>/<int:id>/',views.delete_product,name = 'delete_product'),


]

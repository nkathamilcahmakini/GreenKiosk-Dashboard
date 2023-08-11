from django.urls import path
from .views import edit_product_view, product_detail_view, product_upload_view, products_list

urlpatterns = [
    path("products/upload/", product_upload_view, name = "product_upload_view"),
    path("products/list/", products_list, name= "products_list"),
    path("products/<int:id>/", product_detail_view, name="product_detail_view"),
    path("products/edit/<int:id>/", edit_product_view, name="product_edit_view")
]
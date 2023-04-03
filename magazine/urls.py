from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView,CartDetailView,CategoryListView, OrderDetailView, OrderListView, CartListView

urlpatterns = [
    path('products/', ProductListView),
    path('product/<int:pk>', ProductDetailView),
    path('categories/', CategoryListView),
    path('category/<int:pk>', CategoryDetailView),
    path('carts/', CartListView),
    path('cart/<int:pk>', CartDetailView),
    path('orders/', OrderListView),
    path('order/<int:pk>', OrderDetailView)
]
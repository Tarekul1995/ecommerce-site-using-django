from django.urls import path
from .import views

app_name = 'cart'

urlpatterns = [
    path('<int:object_id>/add_cart/', views.add_cart, name='add_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('<int:object_id>/index/cart_remove/', views.cart_remove, name='cart_remove')
]

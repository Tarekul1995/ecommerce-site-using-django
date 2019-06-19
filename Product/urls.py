from django.urls import path
from .import views

app_name='product'

urlpatterns = [
    path('', views.Home_page.as_view(), name='home'),
    path('<int:pk>/<slug:slug>/', views.product_detail.as_view(), name='product_detail'),
]
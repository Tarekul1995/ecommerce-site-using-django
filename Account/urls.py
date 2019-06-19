from django.urls import path
from .import views

app_name='account'

urlpatterns = [
    path('SignUp/', views.SignUp.as_view(), name='sign_up'),
    path('SignIn/',views.SignIn.as_view(), name='sign_in')
]
from django.urls import path
from goodapp.views import test, aboutUs, Champagne, Cognac, contact, login, PinkWine, RedWine, registration, Rum, SparklingWine, WhiteWine, ProfileView,Products,Cart,createProduct, ProductUpdateView, ProductDeleteView, product
from django.contrib.auth import views as auth_views
from goodapp.forms import LoginForm

urlpatterns = [
    path('', test, name="test"),
    path('aboutUs/', aboutUs, name="aboutUs"),
    path('Champagne/', Champagne, name="Champagne"),
    path('Cognac/', Cognac, name="Cognac"),
    path('contact/', contact, name="contact"),
    # path('login/', login, name="login"),
    path('PinkWine/', PinkWine, name="PinkWine"),
    path('RedWine/', RedWine, name="RedWine"),
    path('registration/', registration, name="registration"),
    path('Rum/', Rum, name="Rum"),
    path('SparklingWine/', SparklingWine, name="SparklingWine"),
    path('WhiteWine/', WhiteWine, name="WhiteWine"),
    path('Products/', Products, name="Products"),
    path('Cart/', Cart, name="Cart"),
    path('accounts/login', auth_views.LoginView.as_view(template_name="goodapp/accounts/Login1.html",authentication_form=LoginForm), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name="goodapp/accounts/Login1.html"), name='logout'),
    path('accounts/profile', ProfileView.as_view(), name='profile'),
    path('create-a-new-product/', createProduct, name='createProductPage'),
    path('update/<pk>', ProductUpdateView.as_view(template_name='goodapp/UpdateProduct.html'), name='updateProductPage'),
    path('delete/<pk>', ProductDeleteView.as_view(template_name='goodapp/DeleteProduct.html'), name='deleteProductPage'),
    path('product/<id>', product, name='productPage'),
]
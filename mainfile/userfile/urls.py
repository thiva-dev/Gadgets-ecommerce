from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('product/', views.product, name="product"),
    path('signin/',views.signin, name="signin"),
    path('login/',views.login, name="login"),
    path('cart_view/',views.Cart, name="cart_view"),
    path('adminproduct/', views.uploadProduct, name="adminproduct"),
    path('search/' ,views.search_data, name="search"),
    path('addcart/<int:prod_id>/', views.addtocart, name="addtocart"),
    path('removecart/<int:prod_id>/', views.deletocart, name="removecart"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
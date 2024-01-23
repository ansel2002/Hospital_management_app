from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.about,name="dashboard"),
    path('about',views.about,name="about"),
    path('cart',views.cart,name="cart"),
    path('thankyou',views.thankyou,name="thankyou"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('store',views.store,name="store"),
    path('shop-single',views.shop,name="shop"),
    path('checkout',views.checkout,name="checkout"),
    path('addItem',views.addItem,name='addItem'),
    path('removeItem',views.removeQnty,name='remove'),
    path('addQnty',views.addQnty,name='addQnty'),
]


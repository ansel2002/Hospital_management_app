from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.about,name="dashboard"),
    path('aboutUs',views.about,name="aboutUs"),
    path('cart',views.cart,name="cart"),
    path('thankyou',views.thankyou,name="thankyou"),
    path('homePage',views.homePage,name="homePage"),
    path('contactUs',views.contact,name="contactUs"),
    path('addProduct',views.addProduct,name="addProduct"),
    path('store',views.store,name="store"),
    path('updateStore',views.updateStore,name="updateStore"),
    path('shop-single',views.shop,name="shop"),
    path('checkout',views.checkout,name="checkout"),
    path('catelogue',views.catelogue,name="catelogue"),
    path('deleteProduct/<str:id>/',views.deleteProduct,name="deleteProduct"),
    path('editProduct/<str:id>/',views.editProduct,name="editProduct"),

    # path('addItem',views.addItem,name='addItem'),
    # path('removeItem',views.removeQnty,name='remove'),
    # path('addQnty',views.addQnty,name='addQnty'),
]


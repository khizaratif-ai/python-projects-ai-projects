from django.urls import path

from . import views



urlpatterns = [

    path(
        '',
        views.menu,
        name='menu'
    ),


    path(
        'add-to-cart/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),


    path(
        'cart/',
        views.cart,
        name='cart'
    ),


    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

]
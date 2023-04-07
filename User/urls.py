from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('register',views.register),
    path('about',views.about),
    path('ViewDetails/<id>',views.ViewDetails),
    path('ShowMedicines/<id>',views.ShowMedicines),
    path('allmedicines',views.allmedicines),
    path('removeItem',views.removeItem),
    path('signout',views.signout),
    path('contact',views.contact),
    path('nav',views.nav),
    path('addToCart',views.addToCart),
    path('thankyou',views.thankyou),
    path('cthankyou',views.cthankyou),
    path('MakePayment',views.MakePayment),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('carousel',views.carousel),
    path('ShippingDetails',views.ShippingDetails),
    path('store',views.store),
]


from django.urls import path


from . import views


urlpatterns=[
      path('',views.store,name="store"),
      path('main',views.main,name="main"),
      path('cartes',views.cartes,name="cartes"),
      path('checkout',views.checkout,name="checkout"),
      path('offer',views.offer,name="offer"),
      path('login',views.login,name="login"),
  
]
from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login ,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.volunteersignup import VolunteerSignup
from .views.orders import OrderView
#from .views.home import inform
from .middlewares.auth import auth_middleware
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',Index.as_view(), name='homepage'),
    path('VolunteerSignup',VolunteerSignup.as_view(),name = 'volunteersignup'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
path('orders', OrderView.as_view(), name='orders'),
#path('aboutourwebsite',inform , name='infom'),
]
urlpatterns += staticfiles_urlpatterns()
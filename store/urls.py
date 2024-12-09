from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('', signup, name='signup'),
    path('home/', home, name='home'),
    path('fruits/', fruits, name='fruits'),
    path('cart/', cart, name='cart'),
    path('contact_me/', contact_me, name='contact_me'),
]
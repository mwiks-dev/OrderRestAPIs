from django.urls import path
from .views import CustomerCreateView, OrderCreateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('customers/', CustomerCreateView.as_view(), name='create-customer'),
    path('orders/', OrderCreateView.as_view(), name='create-order'),
]
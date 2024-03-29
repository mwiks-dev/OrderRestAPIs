from django.urls import path
from .views import CustomerCreateView, OrderCreateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('api/customer/', CustomerCreateView.as_view(), name='create-customer'),
    path('api/order/', OrderCreateView.as_view(), name='create-order'),
]
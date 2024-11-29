from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('login/',views.login),
    path('payment/', views.donate, name='payment_success'),

]
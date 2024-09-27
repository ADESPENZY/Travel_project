from django.urls import path
from . import views 
from account import views as account_views  

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', account_views.login_page, name='login_page'),
    path('destination/', views.destination_page, name='destination_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
]
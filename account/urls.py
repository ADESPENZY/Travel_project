from django.urls import path
from . import views 

urlpatterns = [
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.register_page, name='register_page')
]
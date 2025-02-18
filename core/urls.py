from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contato/', views.contact, name='contact'),
    path('produto/', views.prodruct, name='produto'),
    path('login/', views.login, name='login')
]

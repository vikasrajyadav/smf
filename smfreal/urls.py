from django.urls import path
from . import views

app_name = 'smfreal'

urlpatterns = [
    path('', views.index, name='index'),
    path('fundlist/',views.user_page, name='fund'),
    path('nav/',views.navbarfunction,name='navbar'),
    path('registration/',views.register,name='form'),
    path('equity/',views.equity,name='equity'),
    path('debt/',views.debt,name='debt'),
    path('hybrid/',views.hybrid,name='hybrid'),
]

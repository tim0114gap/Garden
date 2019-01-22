from django.urls import path, include

from . import views

app_name = 'Garden'
urlpatterns = [
    path('', views.index, name='index'),
    path('registerAcount/', views.registerAcount, name='registerAcount'),
    path('loginAcount/',views.loginAcount, name='loginAcount')
]

from django.urls import path

from . import views

app_name = 'Garden'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('registerAcount/', views.registerAcount, name='registerAcount'),
    path('loginAcount/',views.loginAcount, name='loginAcount')
]

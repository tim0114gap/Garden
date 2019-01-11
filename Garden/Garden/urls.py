from django.urls import path

from . import views

app_name = 'Garden'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login')
]

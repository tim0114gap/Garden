from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('garden/',include('Garden.urls')),
    path('admin/', admin.site.urls),
]

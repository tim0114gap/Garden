from django.contrib import admin
from django.urls import include,path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('garden',include('Garden.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='registration/home.html'), name='home'),
    path('admin/', admin.site.urls),
]

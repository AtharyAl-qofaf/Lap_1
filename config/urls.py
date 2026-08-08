from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('doctors/', include('doctors.urls')),
    path('services/', include('services.urls')),
    path('', lambda request: redirect('login')),
]
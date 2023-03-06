from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mailsapp/', include('mailsapp.urls')),
    path('admin/', admin.site.urls),
]

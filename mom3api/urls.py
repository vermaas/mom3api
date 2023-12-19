
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('mom3api/', include('mom3.urls')),
    path('mom3api/admin/', admin.site.urls),
    path('mom3api/api-auth/', include('rest_framework.urls')),
]

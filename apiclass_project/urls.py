
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apiclass_app.urls')),
    path('api/blog/',include('generic_viewset_app.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add url app
    path('', include('restaurant.urls')),
]

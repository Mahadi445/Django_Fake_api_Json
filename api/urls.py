from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dict/',views.Json_data),
    path('product/',views.product),
]

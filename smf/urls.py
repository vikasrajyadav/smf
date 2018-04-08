from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from smfreal import views

urlpatterns = [
    path('', include('smfreal.urls')),
    path('admin/', admin.site.urls),
]

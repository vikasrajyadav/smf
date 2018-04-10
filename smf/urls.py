from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from smfreal import views
from django.contrib.auth import views


urlpatterns = [
    path('', include('smfreal.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/',views.login,name='login'),
    path('accounts/logout/',views.logout,name='logout',kwargs={'next_page':'/'}),
]

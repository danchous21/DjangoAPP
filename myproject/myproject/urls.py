from django.contrib import admin
from django.urls import path
from menu.views import menu_view, services_view, about_view, web_development_view, mobile_development_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_view, name='home'),
    path('menu/', menu_view, name='menu_view'),
    path('services/', services_view, name='services'),
    path('about/', about_view, name='about'),
    path('services/web-development/', web_development_view, name='web_development'),
    path('services/mobile-development/', mobile_development_view, name='mobile_development'),
]

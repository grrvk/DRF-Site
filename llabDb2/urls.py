"""llabDb2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from llab2 import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('list/transport/', views.transport_search_view, name='transport-search-list'),
    path('list/routes/', views.routes_search_view, name='routes-search-list'),
    path('list/cities/', views.cities_search_view, name='cities-search-list'),

    path('admin/', admin.site.urls),
    path('api/', include('llab2.urls')),  # api
    path('api/search/', include('search.urls')),
    path('api/transport/', include('transport.urls')),
    path('api/routers/', include('llabDb2.routers')),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

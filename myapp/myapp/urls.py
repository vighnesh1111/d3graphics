"""myapp URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from page import views
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('intensity', views.intensity, name="intensity"),
    path('likelihood', views.likelihood, name="likelihood"),
    path('relevance', views.relevance, name="relevance"),
    path('year', views.year, name="year"),
    path('country', views.country, name="country"),
    path('topics', views.topics, name="topics"),
    path('region', views.region, name="region"),
    path('sector', views.sector, name="sector"),
    path('search', views.search, name="search"),
    path('sf', views.sf, name="sf"),
    path('sf1', views.sf1, name="sf1"),
    path('sf2', views.sf2, name="sf2"),
    path('sf3', views.sf3, name="sf3"),
    path('sf4', views.sf4, name="sf4"),
    path('sf5', views.sf5, name="sf5"),
    path('sf6', views.sf6, name="sf6"),
    path('sf7', views.sf7, name="sf7"),
    path('sf8', views.sf8, name="sf8"),
]
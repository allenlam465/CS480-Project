"""
comicsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from comicsite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('', views.home),
    path('home/', views.home),
    path('login/', views.loginpage),
    path('loggedin/', views.loggedin),
    path('loggedout/', views.loggedout),
    path('register/', views.register),
    path('registered/', views.registered),
    path('user/<username>', views.user),
    path('myprofile/', views.myprofile),
    path('comic/<int:pageid>/', views.comic),
    path('comic/<int:pageid>', views.comic),
    path('comic', views.comic),
    path('comiclist/', views.comiclist),
    path('comiclist/<slug:sortby>', views.comiclist),
    path('search', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from rest_framework import routers
from core.cart_api import ProductViewSet, CartViewSet, UserViewSet
from core import views as core_views



router  =routers.DefaultRouter()
router.register(r'add-product', ProductViewSet)
router.register(r'add-user', UserViewSet)
router.register(r'create-cart', CartViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', core_views.register, name = 'register'),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^login/$', core_views.user_login, name='login'),
    url(r'^logout/$', core_views.user_logout, name='logout'),
    url(r'', include('core.urls')),
    url(r'api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'api/', include(router.urls)),
    url(r'api/get-user-cart/(?P<user_id>\d+)/', core_views.GetCart.as_view()),
    # url(r'api/get-products/', core_views.GetProducts.as_view())
]


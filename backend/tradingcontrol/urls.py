"""tradingcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from rest_framework_jwt.views import (obtain_jwt_token,
                                      refresh_jwt_token,
                                      verify_jwt_token,)

from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [

    # JWT Path from djangorestframework-jwt
    path('api/v1/token-auth/', obtain_jwt_token),
    path('api/v1/token-refresh/', refresh_jwt_token),
    path('api/v1/token-verify/', verify_jwt_token),

    # Apps path
    # path('api/v1/core/', include('core.urls')),
    # path('api/v1/user/', include('user.urls')),

    # Defaul path
    path('admin/', admin.site.urls),
    path('rest/', include('rest_framework.urls')),
    url(r'^select2/', include('django_select2.urls')),

]

if DEBUG:
    # Serve files from media folder
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
    ]

"""test_mall URL Configuration

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
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    # path('sms_codes/(?P<mobile>1[3-9]\d{9})/', views.SMSCodeView.as_view()),
    re_path(r'^imagecodes/(?P<image_code_id>.+)/$', views.RegisterImageAPIView.as_view(), name='imagecode'),
    re_path(r'^smscodes/(?P<mobile>1[345789]\d{9})/$', views.RegisterSmscodeAPIView.as_view())
    # path(r'^imagecodes/(?P<image_code_id>.+)/$', views.RegisterImageAPIView.as_view(), name='imagecode'),
    # path(r'^smscodes/(?P<mobile>1[345789]\d{9})/$', views.RegisterSmscodeAPIView.as_view())

]

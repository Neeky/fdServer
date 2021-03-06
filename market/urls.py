"""fdServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from market import views

urlpatterns = [
    #增加投资者情况到数据库
    url(r'^add/investorsituation/', views.add_investor_situation),
    #增加shibor利率
    url(r'^add/shiborrate/',views.add_shibor_rate),
    #
    url(r'^add/update/stockindex/',views.add_or_update_stock_index),
    #
    url(r'add/update/foundationbrief/',views.add_foundation_brief),
]

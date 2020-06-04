# -*- coding: utf-8 -*-
"""
@project ： xfz
@Time ： 2020/6/4 15:47
@Auth ： AJay13
@File ：urls.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from django.urls import path
from . import views

app_name='front'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]
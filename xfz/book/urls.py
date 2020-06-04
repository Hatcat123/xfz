# -*- coding: utf-8 -*-
"""
@project ： xfz
@Time ： 2020/6/4 15:30
@Auth ： AJay13
@File ：urls.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from django.urls import path

from book import views

urlpatterns = [
    path('', views.book),
    path('detail/<book_id>/', views.book_detail),
    path('list/', views.book_list),
]

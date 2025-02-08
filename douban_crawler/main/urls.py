from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),# 首页
    path("refresh_movies", views.refresh_movies, name="refresh_movies"),# 刷新电影数据
    path("get_movies", views.get_movies, name="get_movies"),# 获取电影数据
]
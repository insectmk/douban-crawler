from django.urls import path
from . import views

urlpatterns = [
    # 页面
    path("", views.index, name="index"),# 首页
    path("movie", views.movie, name="movie"),# 电影
    path("score", views.score, name="score"),# 评分
    path("word", views.word, name="word"),# 词云
    # 接口
    path("refresh_movies", views.refresh_movies, name="refresh_movies"),# 刷新电影数据
    path("get_movies", views.get_movies, name="get_movies"),# 获取电影数据
]
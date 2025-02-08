from django.http import HttpResponse
from django.shortcuts import render
from . import service

"""
页面：首页
"""
def index(request):
    # 获取所有的电影
    movies = service.get_movies()
    # 给前端传递参数
    context = {"movies": movies}
    # 渲染数据
    return render(request, "main/index.html", context)

"""
页面：电影
"""
def movie(request):
    # 给前端传递参数
    context = {}
    # 渲染数据
    return render(request, "main/movie.html", context)

"""
页面：评分
"""
def score(request):
    # 给前端传递参数
    context = {}
    # 渲染数据
    return render(request, "main/score.html", context)

"""
页面：词云
"""
def word(request):
    # 给前端传递参数
    context = {}
    # 渲染数据
    return render(request, "main/word.html", context)

"""
接口：刷新电影
"""
def refresh_movies(request):
    service.refresh_movies() # 爬取数据，并保存到数据库
    return HttpResponse(service.get_movies())

"""
接口：获取电影
"""
def get_movies(request):
    return HttpResponse(service.get_movies())
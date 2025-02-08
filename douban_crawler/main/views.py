from django.http import HttpResponse
from django.shortcuts import render
from . import service

"""
首页
"""
def index(request):
    # 获取所有的电影
    movies = service.get_movies()
    # 给前端传递参数
    context = {"movies": movies}
    # 渲染数据
    return render(request, "main/index.html", context)

"""
刷新电影
"""
def refresh_movies(request):
    service.refresh_movies() # 爬取数据，并保存到数据库
    return HttpResponse(service.get_movies())

"""
获取电影
"""
def get_movies(request):
    return HttpResponse(service.get_movies())
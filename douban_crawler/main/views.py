from django.http import HttpResponse
from . import service

"""
首页
"""
def index(request):
    return HttpResponse(service.get_movies())

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
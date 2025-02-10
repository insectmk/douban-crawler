from django.http import HttpResponse # 响应
from django.shortcuts import render # 模版渲染
from . import service # 服务类

"""
页面：首页
"""
def index(request):
    rating_range = service.get_rating_range() # 获取评分范围
    # 给前端传递参数
    context = {
        "movies_count": len(service.get_movies()),  # 电影数量
        "rating_range": f"{rating_range['min_rating']}~{rating_range['max_rating']}",  # 评分范围
        "words_count": len(list(service.cut_dada())),  # 词汇统计
    }
    # 渲染数据
    return render(request, "main/index.html", context)

"""页面：电影
参数：
    page_num：第几页
"""
def movie(request):
    # 查询电影
    page_num = request.GET.get("p")
    # 处理 没有传页数
    if page_num is None or page_num == '':
        page_num = 1  # 默认为第一页
    page_num = int(page_num) # 获取参数，转为int
    movies_page = service.get_movies_page(page_num=page_num)
    # 给前端传递参数
    context = {
        'movies': movies_page['movies'], # 电影列表
        'cur_page': movies_page['page_num'], # 当前页
        'page_size': movies_page['page_size'], # 每页行数
        'pages': range(1, movies_page['total_pages']+1), # 总页数列表
        'total_pages': movies_page['total_pages'], # 总页数
    }
    print(context, '传递内容')
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
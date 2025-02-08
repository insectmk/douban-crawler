from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import time
import random # 随机数
from .models import Movies # 电影模型

#要爬取的网页链接
baseurl = "https://movie.douban.com/top250?start="
# 创建正则表达式对象，标售规则   影片详情链接的规则
find_detail_url = re.compile(r'<a href="(.*?)">')# 详情链接
find_img_url = re.compile(r'<img.*src="(.*?)"', re.S)# 图片地址
find_names = re.compile(r'<span class="title">(.*)</span>')# 电影名称
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')# 评分
find_num_judge = re.compile(r'<span>(\d*)人评价</span>') # 评价人数
find_inq = re.compile(r'<span class="inq">(.*)</span>') # 简述
find_other_info = re.compile(r'<p class="">(.*?)</p>', re.S) # 相关信息

"""
获取所有的电影
"""
def get_movies():
    # 获取所有电影数据，并根据排名排序
    return Movies.objects.all().order_by('rank')

"""
爬取豆瓣top250电影数据
"""
def get_data_from_web():
    movies = []  # 用来存储爬取的网页信息
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        # 随机延时
        delay = random.uniform(1, 5)
        time.sleep(delay)
        url = baseurl + str(i * 25)
        html = ask_url(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串
            data = {}  # 保存一部电影所有信息
            item = str(item)
            data['detail_url'] = re.findall(find_detail_url, item)[0]  # 详情链接
            data['img_url'] = re.findall(find_img_url, item)[0]  # 图片链接
            names = re.findall(find_names, item)  # 电影名称
            if len(names) == 2:
                data['name'] = names[0]  # 电影名
                data['name_foreign'] = names[1].replace("/", "")  # 外国电影名
            else:
                data['name'] = names[0]  # 电影名
                data['name_foreign'] = ''  # 外国电影名，为空
            data['rating'] = float(re.findall(find_rating, item)[0])  # 评分
            data['num_judge'] = int(re.findall(find_num_judge, item)[0])  # 评价数
            inq = re.findall(find_inq, item)  # 简述
            if len(inq) != 0:
                data['inq'] = inq[0].replace("。", "")  # 简述
            else:
                data['inq'] = ""  # 简述，为空
            other_info = re.findall(find_other_info, item)[0]
            other_info = re.sub('<br(\\s+)?/>(\\s+)?', "", other_info)
            other_info = re.sub('/', "", other_info)
            data['other_info'] = other_info.strip()  # 相关信息
            movies.append(data)  # 加入到电影集合中
    return movies

"""
将爬取的数据保存到数据库
"""
def refresh_movies():
    # 删除旧的数据
    Movies.objects.all().delete()
    # 获取爬取的数据
    movies_data = get_data_from_web()
    # 遍历数据并保存到数据库
    for index, movie_data in enumerate(movies_data):
        movie = Movies(
            rank=index + 1,  # 假设排名是顺序递增的
            detail_url=movie_data['detail_url'],
            img_url=movie_data['img_url'],
            name=movie_data['name'],
            name_foreign=movie_data['name_foreign'],
            rating=movie_data['rating'],
            num_judge=movie_data['num_judge'],
            inq=movie_data['inq'],
            other_info=movie_data['other_info']
        )
        movie.save()  # 保存到数据库
    return len(movies_data)

"""
得到指定一个URL的网页内容
"""
def ask_url(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head, )
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

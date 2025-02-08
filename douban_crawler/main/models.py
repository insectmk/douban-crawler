from django.db import models

"""
电影
"""
class Movies(models.Model):
    rank = models.IntegerField(default=0)#排名
    detail_url = models.CharField(max_length=2000)#电影详情链接
    img_url = models.CharField(max_length=2000)#图片链接
    name = models.CharField(max_length=200)#影片中文名
    name_foreign = models.CharField(max_length=200)#影片外国名
    rating = models.FloatField(default=0.0)#评分
    num_judge = models.BigIntegerField(default=0)#评价数
    inq = models.CharField(max_length=2000)#简述
    other_info = models.CharField(max_length=2000)#相关信息
    # 打印
    def __str__(self):
        return (f"电影: {self.name} (排名: {self.rank}, 评分: {self.rating}, "
                f"评价数: {self.num_judge}, 国外名称: {self.name_foreign}, 简述: {self.inq})")
from django.http import HttpResponse

# 第一个视图
def index(request):
    return HttpResponse("Hello world!")
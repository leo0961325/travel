from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime #導入時間
from .models import Post

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
#render(request, template_name, dictionary) render是渲染 後面是格式

def index(request):
    return HttpResponse("Hello, world. You're at the trip index.")

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post}) #傳進子介面所需
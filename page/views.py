from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here
def home(request):
    # Post.objects는 쿼리셋이다.
    posts = Post.objects.all() #쿼리셋 메소드, all이라는 메소드는 DB 데이터 집합을 불러온다.
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})
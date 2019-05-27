from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here
def home(request):
    # Post.objects는 쿼리셋이다.
    posts = Post.objects.all() #쿼리셋 메소드, all이라는 메소드는 DB 데이터 집합을 불러온다.
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.content = request.POST['content']
        # image 파일이 있으면 post 객체에 저장
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/detail/'+str(post.id))
    return render(request, 'new.html')
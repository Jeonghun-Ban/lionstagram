from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # post queryset
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})
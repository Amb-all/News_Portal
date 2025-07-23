from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def news_list(request):
    posts = Post.objects.filter(post_type='NW').order_by('-created_at')
    return render(request, 'news/news_list.html', {'posts': posts})
from django.shortcuts import render

def article_list(request):
    posts = Post.objects.filter(post_type='AR').order_by('-created_at')
    return render(request, 'news/article_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    posts = Post.objects.select_related('category', 'location', 'author').filter(is_published=True, category__is_published=True).order_by('-pub_date')
    return render(request, 'blog/index.html', {'post_list': posts})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = category.post_set.filter(is_published=True).select_related('location', 'author').order_by('-pub_date')
    return render(request, 'blog/category.html', {'category': category, 'post_list': posts})

def post_detail(request, id):
    post = get_object_or_404(Post.objects.select_related('category', 'location', 'author'), pk=id, is_published=True)
    return render(request, 'blog/detail.html', {'post': post})


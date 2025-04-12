from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm  # Добавим форму для поста

def index(request):
    now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    now = timezone.now()
    posts = category.post_set.filter(
        is_published=True,
        pub_date__lte=now
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {'category': category, 'post_list': posts})

def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

# Обновленное представление для профиля с параметром username
def profile(request, username):
    # Получаем пользователя по имени (username)
    user = get_object_or_404(User, username=username)
    
    # Получаем публикации этого пользователя
    posts = Post.objects.filter(author=user).order_by('-pub_date')
    
    return render(request, 'blog/profile.html', {'user': user, 'post_list': posts})

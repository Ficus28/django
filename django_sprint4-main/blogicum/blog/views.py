from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Comment, Post, Category
from .forms import PostForm, RegistrationForm, UserProfileForm, CommentForm


# Главная страница
def index(request):
    now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj})

# Страница категории
def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    now = timezone.now()
    posts = category.post_set.filter(
        is_published=True,
        pub_date__lte=now
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/category.html', {
        'category': category,
        'page_obj': page_obj
    })

def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

# Создание нового поста
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', id=post.id)
    form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

# Страница профиля пользователя
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'blog/profile.html', {
        'user': user,
        'page_obj': page_obj
    })

# Регистрация пользователя
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('blog:profile', username=user.username)
    form = RegistrationForm()
    return render(request, 'registration/registration_form.html', {'form': form})

# Редактирование профиля
@login_required
def edit_profile(request, username):
    if request.user.username != username:
        return redirect('blog:profile', username=request.user.username)
    
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile', username=username)
    form = UserProfileForm(instance=user)
    return render(request, 'blog/edit_profile.html', {'form': form})

# Кастомный выход из системы (разрешает GET)
@login_required
def custom_logout(request):
    logout(request)
    return redirect('blog:index')

# Комментарии
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', id=post.id)
    return redirect('blog:post_detail', id=post.id)

@login_required
def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id=post_id)
    form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
        'post': comment.post
    })

@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
    return redirect('blog:post_detail', id=post_id)

# Управление постами
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id=post.id)
    form = PostForm(instance=post)
    return render(request, 'blog/create.html', {
        'form': form,
        'is_edit': True
    })

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/confirm_delete_post.html', {'post': post})
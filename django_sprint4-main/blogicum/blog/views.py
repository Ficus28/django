from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Post, Category
from .forms import PostForm, RegistrationForm, UserProfileForm
from django.utils import timezone

# Стандартные представления для страниц
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

# Страница профиля
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-pub_date')
    return render(request, 'blog/profile.html', {'user': user, 'post_list': posts})

# Страница регистрации
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Входим в систему после регистрации
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('blog:profile', username=user.username)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

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
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'blog/edit_profile.html', {'form': form})

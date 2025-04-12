from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

def index(request):
    # Получаем текущую дату и время
    now = timezone.now()

    # Запрос, который выбирает только те публикации, которые соответствуют условиям
    posts = Post.objects.filter(
        pub_date__lte=now,  # Публикации, дата которых не позже текущего времени
        is_published=True,  # Публикация опубликована
        category__is_published=True  # Категория опубликована
    ).order_by('-pub_date')[:5]  # Сортируем по дате публикации, от новых к старым, ограничиваем 5 последними

    return render(request, 'blog/index.html', {'post_list': posts})

def category_posts(request, category_slug):
    # Получаем категорию или возвращаем 404, если категория не опубликована
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    
    # Получаем публикации, которые принадлежат этой категории, опубликованы и имеют актуальную дату публикации
    now = timezone.now()
    posts = category.post_set.filter(
        is_published=True,
        pub_date__lte=now  # Публикации с актуальной датой
    ).order_by('-pub_date')  # Сортируем по дате публикации

    return render(request, 'blog/category.html', {'category': category, 'post_list': posts})

def post_detail(request, id):
    # Получаем публикацию по id, проверяя все условия
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        is_published=True,  # Публикация должна быть опубликована
        pub_date__lte=timezone.now(),  # Дата публикации не позже текущего времени
        category__is_published=True  # Категория должна быть опубликована
    )
    return render(request, 'blog/detail.html', {'post': post})



# from django.shortcuts import render, get_object_or_404
# from .models import Post, Category

# def index(request):
#     posts = Post.objects.select_related('category', 'location', 'author').filter(is_published=True, category__is_published=True).order_by('-pub_date')
#     return render(request, 'blog/index.html', {'post_list': posts})

# def category_posts(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug, is_published=True)
#     posts = category.post_set.filter(is_published=True).select_related('location', 'author').order_by('-pub_date')
#     return render(request, 'blog/category.html', {'category': category, 'post_list': posts})

# def post_detail(request, id):
#     post = get_object_or_404(Post.objects.select_related('category', 'location', 'author'), pk=id, is_published=True)
#     return render(request, 'blog/detail.html', {'post': post})


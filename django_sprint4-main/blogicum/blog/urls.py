from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('posts/create/', views.post_create, name='create_post'),

    # Обновляем маршрут для профиля, чтобы он принимал username
    path('profile/<str:username>/', views.profile, name='profile'),  # Новый маршрут с параметром username

    # Добавляем маршрут для выхода из системы
    path('logout/', LogoutView.as_view(), name='logout'),
]

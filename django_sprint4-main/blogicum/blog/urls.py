from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

app_name = 'blog'

urlpatterns = [
    # Главная страница и посты
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('posts/create/', views.post_create, name='create_post'),
    path('create/', views.post_create, name='post_create'),

    # Профиль
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),

    # Аутентификация
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.custom_logout, name='logout'),  # Используем кастомный выход

    # Комментарии
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
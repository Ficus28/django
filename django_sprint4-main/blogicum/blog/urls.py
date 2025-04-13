from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    # Главная страница и посты
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('posts/create/', views.post_create, name='create_post'),

    # Профиль и страницы для пользователей
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),

    # Стандартные пути для регистрации и аутентификации
    path('accounts/', include('django.contrib.auth.urls')),

    # Страница регистрации
    path('registration/', views.registration, name='registration'),
    
    # Выход из системы
    path('logout/', LogoutView.as_view(), name='logout'),

    # Комментарии
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]


# from django.urls import path, include
# from . import views
# from django.contrib.auth.views import LogoutView

# app_name = 'blog'

# urlpatterns = [
#     # Главная страница и посты
#     path('', views.index, name='index'),
#     path('posts/<int:id>/', views.post_detail, name='post_detail'),
#     path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
#     path('posts/create/', views.post_create, name='create_post'),

#     # Профиль и страницы для пользователей
#     path('profile/<str:username>/', views.profile, name='profile'),
#     path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),  # Для редактирования профиля

#     # Стандартные пути для регистрации и аутентификации
#     path('accounts/', include('django.contrib.auth.urls')),

#     # Страница регистрации
#     path('registration/', views.registration, name='registration'),
    
#     # Выход из системы
#     path('logout/', LogoutView.as_view(), name='logout'),

#     path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
#     path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
#     path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

# ]

# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from .models import Category, Location, Post

# # Админка для Category
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # Названия столбцов для списка
#     list_display = ('title', 'slug', 'is_published', 'created_at')
    
#     # Фильтрация и поиск по полям
#     search_fields = ('title', 'slug')
#     list_filter = ('is_published', 'created_at')
    
#     # Генерация slug на основе поля title
#     prepopulated_fields = {'slug': ('title',)}
    
#     # Добавление всплывающих подсказок и локализация
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'slug', 'is_published', 'description')
#         }),
#         (_('Date Information'), {
#             'fields': ('created_at',),
#             'classes': ('collapse',),
#         }),
#     )

#     # Локализованные метки и описания
#     def get_search_results(self, request, queryset, search_term):
#         return queryset.filter(title__icontains=search_term)

# # Админка для Location
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     # Названия столбцов для списка
#     list_display = ('name', 'is_published', 'created_at')
    
#     # Фильтрация и поиск по полям
#     search_fields = ('name',)
#     list_filter = ('is_published', 'created_at')

#     # Локализованные метки и описания
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'description', 'is_published')
#         }),
#         (_('Date Information'), {
#             'fields': ('created_at',),
#             'classes': ('collapse',),
#         }),
#     )

# # Админка для Post
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     # Названия столбцов для списка
#     list_display = ('title', 'author', 'category', 'location', 'pub_date', 'is_published', 'created_at')
    
#     # Фильтрация и поиск по полям
#     search_fields = ('title', 'author__username', 'category__title', 'location__name')
#     list_filter = ('is_published', 'pub_date', 'category', 'location')
    
#     # Организация навигации по датам
#     date_hierarchy = 'pub_date'
    
#     # Локализованные метки и описания
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'author', 'content', 'category', 'location', 'is_published')
#         }),
#         (_('Date Information'), {
#             'fields': ('pub_date', 'created_at'),
#             'classes': ('collapse',),
#         }),
#     )

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post

# Админка для Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Названия столбцов для списка
    list_display = ('title', 'slug', 'is_published', 'created_at')
    
    # Фильтрация и поиск по полям
    search_fields = ('title', 'slug')
    list_filter = ('is_published', 'created_at')
    
    # Генерация slug на основе поля title
    prepopulated_fields = {'slug': ('title',)}
    
    # Локализованные метки и описания
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_published', 'description')
        }),
        (_('Date Information'), {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

# Админка для Location
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # Названия столбцов для списка
    list_display = ('name', 'is_published', 'created_at')
    
    # Фильтрация и поиск по полям
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')

    # Локализованные метки и описания
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'is_published')
        }),
        (_('Date Information'), {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

# Админка для Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Названия столбцов для списка
    list_display = ('title', 'author', 'category', 'location', 'pub_date', 'is_published', 'created_at')
    
    # Фильтрация и поиск по полям
    search_fields = ('title', 'author__username', 'category__title', 'location__name')
    list_filter = ('is_published', 'pub_date', 'category', 'location')
    
    # Организация навигации по датам
    date_hierarchy = 'pub_date'
    
    # Локализованные метки и описания
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content', 'category', 'location', 'is_published')
        }),
        (_('Date Information'), {
            'fields': ('pub_date', 'created_at'),
            'classes': ('collapse',),
        }),
    )

    # Дополнительные настройки для сортировки по дате
    ordering = ('-pub_date',)

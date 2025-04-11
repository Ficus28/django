from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    search_fields = ('title', 'slug')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Поле slug есть в модели Category

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'location', 'pub_date', 'is_published', 'created_at')
    search_fields = ('title', 'author__username', 'category__title', 'location__name')
    list_filter = ('is_published', 'pub_date', 'category', 'location')
    date_hierarchy = 'pub_date'
   

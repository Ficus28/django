# blog/forms.py

from django import forms
from .models import Post, Category  # Добавляем импорт модели Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'author', 'location', 'category', 'is_published']  # Оставляем поле 'category'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Ограничиваем доступные категории только опубликованными
        self.fields['category'].queryset = Category.objects.filter(is_published=True)  # Доступны только опубликованные категории

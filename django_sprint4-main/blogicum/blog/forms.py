from django import forms
from django.contrib.auth.models import User
from .models import Post, Category, Comment

# Форма для создания или редактирования поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'author', 'location', 'category', 'is_published']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Ограничиваем доступные категории только опубликованными
        self.fields['category'].queryset = Category.objects.filter(is_published=True)

# Форма регистрации
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data

# Форма для редактирования профиля пользователя
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']

# Форма для комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

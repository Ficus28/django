from django import forms
from django.contrib.auth.models import User
from .models import Post, Category, Comment
from django.utils import timezone
from django.contrib.auth.forms import UserChangeForm

# Форма для создания или редактирования поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'is_published', 'image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now()  # Теперь timezone определен

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
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)  # Убираем поле смены пароля
# Форма для комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
        }

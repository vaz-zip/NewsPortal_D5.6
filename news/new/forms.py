from django.forms import ModelForm
from .models import Post, User


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category']


class AuthorForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'user')
        labels = {
            'username':'Your Name',
            'email': 'Your Email',
            'comment_content':'Your Comment'
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'image', 'tag']
        labels = {
            'tag':'Choose The Tags'
        }

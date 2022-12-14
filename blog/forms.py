from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title", "slug", "preparation_time", "cook_time",
            "description", "ingredients", "image", "status")
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }

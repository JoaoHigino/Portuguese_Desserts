from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'description', 'ingredients')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'content')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'recipe', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

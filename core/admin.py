from django.contrib import admin
from .models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tag', 'date')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_created')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

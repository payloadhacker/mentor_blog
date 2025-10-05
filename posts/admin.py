from django.contrib import admin
from posts.models import Author, Post, Tag
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', "bio")
    search_fields = ('user_username',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ( 'name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ( 'title', 'author', 'published', 'published_at')
    list_filter = ('published', 'author',)
    search_fields = ('title', 'body', 'author__user__username')
    prepopulated_fields = {'slug': ('title',)}
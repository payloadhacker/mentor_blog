from django.contrib import admin
from posts.models import Author, Post, Tag
from django.utils import timezone
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
    readonly_fields = ('published_at',)
    def save_model(self, request, obj, form, change):
        if obj.published and obj.published_at is None:
            obj.published_at = timezone.now()
        super().save_model(request, obj, change)
    list_display  = ( 'title', 'author', 'published', 'published_at')
    list_filter = ('published', 'author',)
    search_fields = ('title', 'body', 'author__user__username')
    prepopulated_fields = {'slug': ('title',)}
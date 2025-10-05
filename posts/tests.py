from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Author, Post, Tag
from django.contrib import admin
from posts.admin import PostAdmin


class AdminTest(TestCase):
    def test_post_admin_registrationa(self):
        self.assertIsInstance(admin.site._registry.get(Post), PostAdmin)

class PostModelTest(TestCase):
    def test_create_post_with_author_and_tag(self):
        user = User.objects.create_user(username="alice", password= 'password123')
        author = Author.objects.create(user=user, bio="A passionate writer.")
        tag = Tag.objects.create(name="django")
        post = Post.objects.create(
            title="My First Post",
            slug="my-first-post",
            body="Hello world!",
            author=author,
            published=True
        )
        post.tags.add(tag)
        self.assertEqual(post.author.user.username, "alice")
        self.assertIn(tag, post.tags.all())

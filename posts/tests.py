from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Author, Post

class PostViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="john", password="password123")
        self.author = Author.objects.create(user=self.user)
        self.post = Post.objects.create(title="My Post", body="Content", author=self.author)

    def test_post_list_view_status_code(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Post")

    def test_post_create_requires_login(self):
        response = self.client.get(reverse("post_create"))
        self.assertNotEqual(response.status_code, 200)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="john", password="password123")
        response = self.client.post(reverse("post_create"), {
            "title": "New Post",
            "body": "Test body"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success

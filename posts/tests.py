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

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Author, Post
from django.urls import reverse

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="pass123")
        self.author = Author.objects.create(user=self.user)
        self.client.login(username="alice", password="pass123")
        self.post = Post.objects.create(title="My Post", body="Hello", author=self.author)

    def test_list_posts(self):
        response = self.client.get(reverse("api_post_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("My Post", str(response.data))

    def test_create_post(self):
        data = {"title": "New API Post", "body": "This is via API."}
        response = self.client.post(reverse("api_post_list_create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_own_post(self):
        data = {"title": "Updated", "body": "Changed body"}
        response = self.client.put(reverse("api_post_detail", args=[self.post.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_own_post(self):
        response = self.client.delete(reverse("api_post_detail", args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

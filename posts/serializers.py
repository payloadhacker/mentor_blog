from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.user.username")

    class Meta:
        model = Post
        fields = ["id", "title", "body", "author", "author_username", "created_at", "updated_at"]
        read_only_fields = ["author"]

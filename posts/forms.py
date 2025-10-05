from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'published']
        widgets = {'body': forms.Textarea(attrs={'rows': 5}),}

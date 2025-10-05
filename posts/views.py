from django.views.generic import CreateView, DeleteView,UpdateView, ListView, DetailView
from posts.models import Post, Author
from django.urls import reverse_lazy
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-published_at")

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        post = form.save(commit=False)
        # temporary: assign first author
        default_author = Author.objects.first()
        if default_author is None:
            return super().form_invalid(form)
        post.author = default_author
        post.save()
        return super().form_valid(form)

    

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    successful_url = reverse_lazy('post_list')

        
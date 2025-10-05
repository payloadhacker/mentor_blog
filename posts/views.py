from django.views.generic import CreateView, DeleteView,UpdateView, ListView, DetailView
from posts.models import Post, Author
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




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


class PostCreateView(LoginRequiredMixin, CreateView):

    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user=self.request.user)
        post.save()
        return super().form_valid(form)

    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy("post_list")
    def test_func(self):
            post = self.get_object()
            return post.author.user == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    
    model = Post
    template_name = "posts/post_confirm_delete.html"
    successful_url = reverse_lazy('post_list')
    def test_func(self):
        post = self.get_object()
        return post.author.user == self.request.user

        
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Author.objects.create(user=user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form": form}) 
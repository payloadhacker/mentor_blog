from django.urls import path
from posts.views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

from . import views
urlpatterns = [
    path("api-client/", views.client_View, name="api_client"),
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
]

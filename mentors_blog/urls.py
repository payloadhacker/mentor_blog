from django.contrib import admin
from django.urls import path, include
from posts.views import signup_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", signup_view, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("posts.urls")),
    path("api/", include("posts.api_urls")),

]

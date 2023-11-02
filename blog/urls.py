from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("add_post", views.add_post, name="add_post"),
    path("user/<str:username>", views.user_page, name="user_page"),
    path("post_page/<int:post_pk>", views.post_page, name="post_page"),
    path("edit_post/<int:post_pk>/<str:status>", views.post_status, name="edit_post"),
    path("post_vote/<int:post_pk>/<str:direction>", views.post_vote, name="post_vote"),
    path("delete_comment/<int:comment_pk>", views.delete_comment, name="delete_comment"),

    # Authentication
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
]
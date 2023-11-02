from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, User, Comment
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-votes")
    return render(request, "blog/index.html", context={
        "posts": posts,
    })

@login_required(login_url="/login")
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("postTitle")
        content = request.POST.get("postContent")
        print(f"Title: {title} \nContent: {content}")
        post = Post.objects.create(title=title, owner=request.user, content=content)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "blog/add_post.html")


def post_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        text = request.POST.get("postComment")
        Comment.objects.create(user=request.user, text=text, post=post)

        return HttpResponseRedirect(reverse("post_page", args=(post_pk, )))
    
    return render(request, "blog/post_page.html", context={
        "post": post,
        "comments": post.comments.all(),
    })

def post_status(request, post_pk, status):
    post = Post.objects.get(pk=post_pk)
    if status == "delete":
        post.delete()
        return HttpResponseRedirect(reverse("index"))
    
    elif status == "edit":
        if request.method == "POST":
            new_title = request.POST.get("newPostTitle")
            new_content = request.POST.get("newPostContent")

            post.title = new_title
            post.content = new_content
            post.save()
            return HttpResponseRedirect(reverse("post_page", args=(post_pk, )))
        
        return render(request, "blog/edit_post.html", context={
            "post": post,
        })
    
    else:
        return HttpResponseRedirect(reverse("index"))
    
def search(request):
    user_input = request.GET.get("search", "").lower()
    posts = Post.objects.all()
    search_posts = []
    for post in posts:
        if user_input in post.title.lower():
            search_posts.append(post)

    return render(request, "blog/search.html", context={
        "search_posts": search_posts,
        "user_input": user_input
    })

@login_required(login_url="/login")
def user_page(request, username):
    user = User.objects.get(username=username)
    owned_posts = user.owned_posts.all()
    return render(request, "blog/user_page.html", context={
        "user": user,
        "owned_posts": owned_posts,
    })
    
def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    post = comment.post
    Comment.objects.get(pk=comment_pk).delete()

    return HttpResponseRedirect(reverse("post_page", args=(post.pk, )))

@login_required(login_url="/login")
def post_vote(request, post_pk, direction):
    post = Post.objects.get(pk=post_pk)
    if direction == "up_vote":
        post.votes += 1

    elif direction == "down_vote":
        post.votes -= 1

    post.save()
    return HttpResponseRedirect(reverse("index"))


# Authentication

def register_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if passw != confirmation:
            return render(request, "blog/register.html", context={
                "message": "Confirmação de senha incorreta!"
            })
        
        try:
            user = User.objects.create_user(username=user, password=passw)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", context={
                "message": "Este email já está em uso.",
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "blog/register.html")

def login_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        user = authenticate(request, username=user, password=passw)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", context={
                "message": "Email/Senha inválidos!"
            })
        
    return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=64, default="", blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name="owned_posts")
    content = models.TextField()
    votes = models.IntegerField(default=0)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name="made_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=True, related_name="comments")
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.post} = {self.text}"
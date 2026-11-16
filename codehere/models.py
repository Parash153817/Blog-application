from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)
    content=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    is_public=models.BooleanField(default=False)

    def __str__(self):
        return self.title




class Comment(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

    

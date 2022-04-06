from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()


User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
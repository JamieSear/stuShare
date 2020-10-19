from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #time when published
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted then so is post

    def __str__(self):
        return self.title

    def get_absolute_url(self): #find url to any post 
        return reverse('post-detail', kwargs={'pk': self.pk}) #reverse redirects to detail view of new post

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
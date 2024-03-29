from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_Posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title
    
    #this send us to the page of where the new post is 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
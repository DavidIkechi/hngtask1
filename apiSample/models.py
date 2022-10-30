from django.db import models

# Create your models here.
class HNGUser(models.Model):
    slackUsername = models.CharField(max_length=100, blank=False)
    backend = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    bio = models.TextField(blank = False)
    
    def __str__(self):
        return self.slackUsername
    
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(HNGUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
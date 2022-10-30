from django.db import models

# Create your models here.
class HNGUser(models.Model):
    slackUsername = models.CharField(max_length=100, blank=False)
    backend = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    bio = models.TextField(blank = False)
    
    def __str__(self):
        return self.slackUsername
    
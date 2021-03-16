from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text = models.TextField()
  create_date = models.DateTimeField(default=timezone.now())
  published_date = models.DateTimeField(blank=True,null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()
  
  def approve_comments(self):
    return self.comments.filter(approved_comments=True)

  def __str__(self):
    return self.title

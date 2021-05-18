from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    


class Comment(models.Model):
    post =models.ForeignKey("blog.Post", related_name="comments" ,on_delete=models.CASCADE)
    author = models.CharField(max_length=500)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    

    def __str__(self):
        return self.text
    
    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("psot_list", kwargs={"pk": self.pk})
    
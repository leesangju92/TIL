from django.db import models


class Newsfeed(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default="far fa-smile-wink")
    content = models.CharField(max_length=500)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.title} : {self.content}"

class Comment(models.Model):
    newsfeed = models.ForeignKey(Newsfeed, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.title} : {self.content}"

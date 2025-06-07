from django.db import models


class Post(models.Model):
    """Model representing a Post"""

    title = models.CharField(max_length=100)
    body=models.TextField()
    slug = models.SlugField(default="this-is-a-post")
    banner = models.ImageField(default='banner.png', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering=['created_at']

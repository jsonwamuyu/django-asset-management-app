from django.db import models

# Create your models here.


class User(models.Model):
    """
    Represent User
    """
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"] 


    def __str__(self):
        return self.username
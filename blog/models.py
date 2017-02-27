from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    pass


class Blog(models.Model):
    """
    A blog created by user
    """
    user = models.ForeignKey('BlogUser')
    title = models.CharField(max_length=512)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp', )

    @classmethod
    def get_top_10(cls):
        pass

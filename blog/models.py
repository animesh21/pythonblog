from django.db import models
import datetime
from django.utils import timezone
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

    class Meta:
        ordering = ('-timestamp', )

    def __str__(self):
        return self.title

    @classmethod
    def get_top_10(cls):
        blogs = Blog.objects.all().order_by('-timestamp')  # not needed as we've already defined this in Meta class

        if(len(list(blogs))<10):
            return list(blogs)
        else:
            return list(blogs[0:11])

    @classmethod
    def was_publish_recently(cls, self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.timestamp <= now

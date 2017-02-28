from django.test import TestCase
from .models import Blog, BlogUser
from django.utils import timezone


class BlogTest(TestCase):
    """
    tests different methods of Blog model
    """
    def setUp(self):
        user = BlogUser.objects.create(username='animax', email='animesh0721@gmail.com', password='animax')
        blog1 = Blog.objects.create(user=user, title='My first blog', text='Hello, World!')
        blog2 = Blog.objects.create(user=user, title='My second blog', text='Hello, World!')
        blog3 = Blog.objects.create(user=user, title='My third blog', text='Hello, World!')
        a_day = timezone.timedelta(days=1)
        tomorrow = timezone.now() + a_day
        future_blog = Blog.objects.create(user=user, title='Future blog', text='Hello, my future self')
        future_blog.timestamp = tomorrow
        future_blog.save()

    def test_get_top_10(self):
        blogs = Blog.get_top_10()
        blogs_sorted = sorted(blogs, key=lambda x: x.timestamp, reverse=True)
        self.assertEquals(blogs, blogs_sorted)

    def test_was_published_recently(self):
        future_blog = Blog.objects.get(title='Future blog')
        is_recent = Blog.was_publish_recently(future_blog)
        self.assertEquals(is_recent, False)
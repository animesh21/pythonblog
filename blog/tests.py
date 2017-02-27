from django.test import TestCase
from .models import Blog, BlogUser


class BlogTest(TestCase):
    """
    tests different methods of Blog model
    """
    def setUp(self):
        user = BlogUser.objects.create(username='animax', email='animesh0721@gmail.com', password='animax')
        blog1 = Blog.objects.create(user=user, title='My first blog', text='Hello, World!')
        blog2 = Blog.objects.create(user=user, title='My second blog', text='Hello, World!')
        blog3 = Blog.objects.create(user=user, title='My third blog', text='Hello, World!')

    def test_get_top_10(self):
        blogs = Blog.get_top_10()
        blogs_sorted = sorted(blogs, key=lambda x: x.timestamp, reverse=True)
        self.assertEquals(blogs, blogs_sorted)
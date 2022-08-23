from django.test import TestCase
from .models import Blog
# Create your tests here.


class POSTTestCase(TestCase):

    def setUp(self):
        self.blog = Blog.objects.create(title='django', author='harouna', slug='django')

    def test_post_blog(self):
        d = self.blog
        self.assertTrue(isinstance(self.blog, Blog))
        self.assertEqual(str(d), 'django')

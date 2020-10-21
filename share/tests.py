from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

User = get_user_model()

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='thispassword')
        self.userj = User.objects.create_user(username='jim', password='thispassword2')
        Post.objects.create(content="hello there 1", author=self.user)
        Post.objects.create(content="hello there 2", author=self.user)
        Post.objects.create(content="hello there 3", author=self.userj)
        self.currentCount = Post.objects.all().count()

    def test_post_created(self):
        post_obj = Post.objects.create(content="hello there 4", author=self.user)
        self.assertEqual(post_obj.id, 4)
        self.assertEqual(post_obj.author, self.user)

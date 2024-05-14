from django.test import TestCase
from app.models import Post
from datetime import datetime
# Create your tests here.

class PostTestCase(TestCase):
    def testPost(self):
        now =  datetime.now()
        post = Post(temp = 72.22, dateTime = now)
        self.assertEqual(post.temp, 72.22)
        self.assertEqual(post.dateTime, now)
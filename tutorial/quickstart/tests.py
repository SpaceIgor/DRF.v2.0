#from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from tutorial.quickstart.models import Post, Comment, Category, Author
from rest_framework import status
import json
import coverage



cov = coverage.Coverage()
cov.start()


client = APIClient()



class PostTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='ihor', password='RYcdKc4BW9rk-*2')
        self.user_token = Token.objects.create(user=self.user)
        self.category = Category.objects.create(category_name='Ноутбуки', slug='laptop')

        self.new_author = Author.objects.create(
            author_name="Ihor",
            email="igorsivak97@gmail.com",
        )

        self.correct_post = {
            'post_text': 'Name Post',
            'slug': 'name-post',
            'author': 1,
            'category': 1,
        }

        self.wrong_post = {
            'post_text': '',
            'slug': '',
            'author': 1,
            'category': 1,
        }

        Post.objects.create(
            post_text='Name name Post',
            slug='name-name-post',
            author=self.new_author,
            category=self.category,
        )

    def test_create_correct_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post('/api/post/', data=json.dumps(self.correct_post),
        content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)


    def test_create_wrong_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post('/api/post/', data=json.dumps(self.wrong_post),
        content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 1)


    def test_post_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.get('/api/post/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        correct_comment = {
            "text": "Good!",
            "post": 1,
            "author": 1

        }

        response = self.client.post('/api/comment/', correct_comment)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Post.objects.get(pk=1).post_comments.count(), 1)
        self.assertEqual(Post.objects.get(pk=1).post_comments.get(pk=1).text, "Good!")

    def test_change_author_status(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        self.task = change_author_status()
        self.assertEqual(Author.objects.get().is_notified, True)


cov.stop()
cov.save()

cov.html_report()









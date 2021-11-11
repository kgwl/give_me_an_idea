from django.test import TestCase,Client
from django.urls import reverse
from idea_generator.models import Idea,Category,Difficulties
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')


    def test_index_view_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'main.html')



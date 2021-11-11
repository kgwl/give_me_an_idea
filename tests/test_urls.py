from django.test import SimpleTestCase
from django.urls import reverse,resolve
from idea_generator.views import index_view


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolve(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func,index_view)

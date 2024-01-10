from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()


class IndexViewTest(TestCase):
    def test_index_get(self):
        response = client.get('/restaurant/')
        assert response.status_code == 200


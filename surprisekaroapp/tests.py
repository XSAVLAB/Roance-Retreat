from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class MyViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

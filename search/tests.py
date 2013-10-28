from django.test import TestCase

class SearchTest(TestCase):
    
    def test_search_page_exists(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

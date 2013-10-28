from django.test import TestCase

class SearchTest(TestCase):
    
    def test_search_page_exists(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_site_index_is_searchpage(self):
        index_response = self.client.get('/')
        search_response = self.client.get('/search/')
        self.assertEqual(index_response.content, search_response.content)

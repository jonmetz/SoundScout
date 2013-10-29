from django.test import TestCase


class HomepageTests(TestCase):
    
    def does_page_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

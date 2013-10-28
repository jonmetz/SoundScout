from django.test import TestCase

from songs.models import Song

class TestTests(TestCase):
    def testtesttestcase(self):
        self.assertEqual(1, 1)

class SongTests(TestCase):
    def setUp(self):
        s = Song(url = "fake", title = "fake", artist = "fake", artwork = "a")
        s.save()

    def test_if_the_view_for_the_first_exists(self):
        """
        Fail if view for the song with id == 1 fails to render
        """        
        test_song = Song.objects.get(title="fake")
        response = self.client.get('/songs/'+str(test_song.pk)+'/')
        self.assertEqual(response.status_code, 200)
        

class SearchTest(TestCase):
    
    def test_search_page_exists(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

import threading
from django.shortcuts import render
import requests
from songs.models import Song

def searchpage(request):
    context = []
    return render(request, 'search/search.html', context)

def searchform(request):
    return results(request, request.GET['q'])

def find_query(search_terms):
    api = ""
    r1 = requests.get("".join([api, search_terms])
    if r1.json()["total_results"]:
        hyped_results = r1.json()["songs"][0:15]
        for result in hyped_results:
            new_song = Song()
            new_song.downloads = 0
            new_song.title =  result['song_name']
            new_song.artist =  result['song_artist']
            new_song.artwork =  result['song_image']
            url_of_mp3_url = ""+result['song_id']
            new_song.url = requests.get(url_of_mp3_url).content.strip('\t\n')
            new_song.save()
        return True
    else:
        return False


def display_search_results(request, search_terms, refresh=False):
    if search_terms != '':
        results = list(set(Song.objects.filter(title__icontains=search_terms) | Song.objects.filter(artist__icontains=search_terms)))[0:20]
    else:
        context = {'search_terms': search_terms}
        return render(request, 'search/just_a_sec.html', context)
    if not results and refresh:
        context = {'search_terms': search_terms}
        t = threading.Thread(target=find_query, args=[search_terms])
        t.start()
        return render(request, 'search/just_a_sec.html', context)
    else:        
        context = {'found': True, 'results': results}
        return render(request, 'search/results.html', context)

def results(request, search_terms):
    return display_search_results(request, search_terms, refresh=True)

def looked_for(request, search_terms):
    return display_search_results(request, search_terms, refresh=False)


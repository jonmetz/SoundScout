from django.shortcuts import render, get_object_or_404

from songs.models import Song

def song(request, song_id):
    song_info = get_object_or_404(Song, pk=song_id)
    song_info.downloads += 1
    song_info.save()
    context = {'url': song_info.url}
    return render(request, 'songs/song.html', context)

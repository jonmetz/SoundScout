from django.shortcuts import render, get_object_or_404

from songs.models import Song

def song(request, song_id):
    song_info = get_object_or_404(Song, pk=song_id)
    context = {'song_info': song_info}
    return render(request, 'songs/song.html', context)

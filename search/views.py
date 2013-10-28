from django.shortcuts import render

def searchpage(request):
    return render(request, 'search/search.html', [])


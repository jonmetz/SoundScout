from django.shortcuts import render

def index(request):
    return render(request, 'search/search.html', [])

def page_does_not_exist(request, title):
    return render(request, 'coming_soon.html', {"title": title})

def browse(request):
    return page_does_not_exist(request, "Browse")

def about(request):
    return page_does_not_exist(request, "About")

def contact(request):
    return page_does_not_exist(request, "Contact")

def legal(request):
    return page_does_not_exist(request, "Legal")

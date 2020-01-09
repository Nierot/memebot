from django.shortcuts import render

def memeView(request):
    return render(request, 'meme.html')
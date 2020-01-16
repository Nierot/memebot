import os
import random
import ntpath

from django.shortcuts import render
from django.http import HttpResponse

from meme.images import randomImage, download

def memeView(request):
    meme = randomImage()
    context = {'meme': meme}
    return render(request,'meme/index.html',context=context)

def downloadView(request):
    #download("animemes")
    return HttpResponse("oof")
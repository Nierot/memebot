import os
import random

from django.shortcuts import render
from django.http import HttpResponse

from meme.images import randomImage, randomImgbb

def memeView(request):
    meme = randomImgbb()
    print(meme)
    context = {'meme':meme}
    return render(request,'meme/index.html',context=context)
    
    
    #image_data = open(randomImage("o"), "rb").read()
    #print(randomImage('d'))
    #return HttpResponse(image_data, content_type="image/jpeg")
import os
import random

from django.shortcuts import render
from django.http import HttpResponse

from meme.images import randomImage

def memeView(request):
    image_data = open(randomImage("o"), "rb").read()
    return HttpResponse(image_data, content_type="image/jpeg")
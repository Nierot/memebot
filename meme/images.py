import os
import random
import requests
import os
import ntpath
import re
import string
from meme.models import Meme
from memebot.settings import BASE_DIR

PATH = os.path.join(BASE_DIR, "static") #os.path.join(os.path.dirname(__file__),"memes")

files = []

def randomImage():
    for r, d, f in os.walk(PATH):
        for file in f:
            if '.jpg' or '.jpeg' or '.png' in file:
                files.append(os.path.join(r, file))
    file = random.choice(files)
    file = ntpath.basename(file)
    return file

def download(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '.json?&limit=100'
    response = requests.get(url, headers={'User-agent': 'nierot 0.1'})
    memesPATH = os.path.join(PATH,"/memes")
    if not response.ok:
        print("Error: " + str(response.status_code))
        exit()

    data = response.json()['data']['children']
    i = 0
    j = 0
    while i < len(data):
        j = 0
        firstPost = data[i]['data']
        imageUrl = firstPost['url']

        print("Currently trying to download: " + imageUrl)

        if '.png' in imageUrl:            
            extension = '.png'        
        elif '.jpg' in imageUrl or '.jpeg' in imageUrl:            
            extension = '.jpeg'
        elif 'imgur' in imageUrl:
            print('oof')
            imageUrl += '.jpeg'
            extension = '.jpeg'
        else:
            print("Not an image")
            i += 1
            continue

        image = requests.get(imageUrl, allow_redirects=False)
        if (image.status_code == 200):
            print("Saving image to: " + PATH + str(i) + extension)
            i += 1
            name = randomID()
            path = PATH + "/memes" + name + extension
            meme = Meme(name=randomID(),url = path)
            meme.save()
            open(path, 'wb').write(image.content)
        else:
            print("nee")
            i += 1

def randomID():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

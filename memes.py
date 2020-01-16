import requests
import os
import pycurl
import re

subreddit  = "me_irl"
url = 'https://www.reddit.com/r/' + subreddit + '.json?&limit=100'
PATH = os.path.join(os.path.dirname(__file__),"meme/memes/" + subreddit + "/")
response = requests.get(url, headers={'User-agent': 'nierot 0.1'})

if not response.ok:
    print("Error: " + str(response.status_code))
    exit()

data = response.json()['data']['children']
i = 0
def method(i):
    while i < len(data):
        firstPost = data[i]['data']
        imageUrl = firstPost['url']

        print("Currently trying to download: " + imageUrl)

        image = requests.get(imageUrl, allow_redirects=False)

        if '.png' or '.jpg' or '.jpeg' in imageUrl:
            imageoof = True
            imageUrl = re.sub('https://i.redd.it/', '', imageUrl)       
        elif 'imgur' in imageUrl:
            imageoof = True
            imageUrl = re.sub('https://i.imgur.com/', '', imageUrl)   
        elif 'comment' in imageUrl:
            print('oof')
            imageoof = False
        else:
            imageoof = False
            print("Not an image")
            i += 1
            continue

        print(image)
        if (image.status_code == 200 and imageoof):
            print("Saving image to: " + PATH + imageUrl)
            open(PATH + imageUrl, 'wb').write(image.content)
            i += 1


method(i)
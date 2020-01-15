import requests
import os
subreddit  = "HistoryMemes"
url = 'https://www.reddit.com/r/' + subreddit + '.json?&limit=100'
PATH = os.path.join(os.path.dirname(__file__),"memebot/static/" + subreddit + "/")
print(PATH)
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

        if '.png' in imageUrl:            
            extension = '.png'        
        elif '.jpg' in imageUrl or '.jpeg' in imageUrl:            
            extension = '.jpeg'
        elif 'imgur' in imageUrl:
            imageUrl += '.jpeg'
            extension = '.jpeg'
        else:
            print("Not an image")
            i += 1
            continue

        image = requests.get(imageUrl, allow_redirects=False)

        if (image.status_code == 200):
            print("Saving image to: " + PATH + str(i) + extension)
            open(PATH + str(i) + extension, 'wb').write(image.content)
            i += 1
        print()


method(i)
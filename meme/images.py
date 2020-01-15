import os
import random

shittyPATH = "/home/nierot/dev/memebot/memebot/static/"
PATH = os.path.join(os.path.dirname(__file__),"memes/")

files = []

def randomImage(subreddit):
    for r, d, f in os.walk(shittyPATH):
        for file in f:
            if '.jpg' or '.jpeg' or '.png' in file:
                files.append(os.path.join(r, file))
    return random.choice(files)

print(randomImage('pf'))
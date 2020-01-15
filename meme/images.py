import os
import random

shittyPATH = "/home/nierot/dev/memebot/static"
PATH = os.path.join(os.path.dirname(__file__),"static")

files = []

def randomImage(subreddit):
    print(PATH)
    for r, d, f in os.walk(PATH):
        for file in f:
            if '.jpg' or '.jpeg' or '.png' in file:
                files.append(os.path.join(r, file))
    return random.choice(files)

#randomImage('f')
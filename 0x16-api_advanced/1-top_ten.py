#!/usr/bin/python3


import sys
import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'Queen'}
    url = url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=headers).json()

    try:
        for d in url.get('data').get('children'):
            print(d.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])

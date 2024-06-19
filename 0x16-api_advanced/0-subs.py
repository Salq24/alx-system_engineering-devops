#!/usr/bin/python3
"""function that queries the reddit api and returns the
num of sbscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """ the function that queries reddit api"""
    headers = {'User-agent': "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

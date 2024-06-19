#!/usr/bin/python3
"""function that queries the reddit api and returns the
num of sbscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """ the function that queries reddit api"""
    headers = {'User-agent': 'Chrome/58.0.3029.110 Safari/537.3'}
    link = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = get(link, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

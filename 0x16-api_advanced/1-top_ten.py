#!/usr/bin/python3
"""This module implements a function that queries a reddit subreddit, for
the top 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """This function prints the top 10 hop post of a valid subreddit.
    if the subreddit is not valid, it returns NONE
    """

    header = {
        "User-Agent": "IFEBUZZ"
        }

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(
            subreddit), headers=header, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        response = response.json().get('data').get('children')
        for child in response:
            data = child.get('data')
            if data.get('title'):
                print(f'{data.get("title")}')

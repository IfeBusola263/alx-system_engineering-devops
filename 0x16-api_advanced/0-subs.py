#!/usr/bin/python3
"""This module implements a function to query the reddit API
for the number of subscribers for a given subreddit.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers of a valid subreddit.
    and zero for an invalid subreddit.
    """

    header = {
        "User-Agent": "IFEBUZZ"
        }
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(
        subreddit), headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0
    response = response.json()
    data = response.get('data')
    numSubscribers = data.get('subscribers')
    return numSubscribers

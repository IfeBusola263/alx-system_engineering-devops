#!/usr/bin/python3
"""This module implements a function that recursively makes a request
to a subreddit to get all the hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This function fetches all the hot articles in subreddit.
    """

    header = {
        "User-Agent": "IFEBUZZ"
        }

    param = {
        "after": after,
        }

    if after is None:
        response = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(
                subreddit), headers=header, allow_redirects=False)
    else:
        response = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(
                subreddit), headers=header,
            allow_redirects=False, params=param)

    if response.status_code != 200:
        return None
    else:
        # print(f'Present after: {response.json().get("data").get("after")}')
        after = response.json().get('data').get('after')
        # print(f'Present Page number of articles:
        # {len(response.json().get("data").get("children"))}')
        hot_list = hot_list + response.json().get('data').get('children')
        # print(f'Present length of Hot articles:   {len(hot_list)}')
        # print('\n\n\=========================
        # ===========================================\n\n')
        # if after is None:
        #     return hot_list

        new_list = recurse(subreddit, hot_list, after)
        if new_list is None or after is None:
            return hot_list
        else:
            return new_list

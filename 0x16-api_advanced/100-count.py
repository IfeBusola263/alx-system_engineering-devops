#!/usr/bin/python3
"""This module implements a count of all the given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """This function counts the number of sorted keywords supplied
    and returns none if the subreddit does not exist.
    """
    if count_dict is None:
        count_dict = {}

    header = {
        'User-agent': 'IFEBUZZ',
        }
    params = {'limit': 25}

    if after:
        params['after'] = after

    ul = 'https://www.reddit.com/r/{}/top.json?sort=top&show=all&t=all'.format(
        subreddit)

    response = requests.get(ul, headers=header, params=params)

    if response.status_code != 200:
        return None

    response_to_json = response.json()
    post_list = response_to_json.get('data', {}).get('children', [])

    for post in post_list:
        title = post['data']['title'].upper()
        for word in word_list:
            if word.upper() in title:
                count_dict[word] = count_dict.get(word, 0) + 1

    after = response_to_json.get('data').get('after')

    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        print_results(count_dict)


def print_results(word_list):
    """Helper function for printing count and word"""
    word_counts = {}
    for word, count in zip(word_list, range(len(word_list))):
        word_counts[word.lower()] = count
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

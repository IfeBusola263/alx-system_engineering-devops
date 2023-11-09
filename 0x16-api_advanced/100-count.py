#!/usr/bin/python3
"""This Module implements a fucntion to count words in
all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.
    """
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'IFEBUZZ'}
    params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        # Parse the titles of the posts after extraction
        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()

            # check for keyword in title and count
            for word in word_list:
                if word.lower() in words:
                    times = words.count(word.lower())
                    counts[word.lower()] = counts.get(word.lower(), 0) + times

        # Check for next page if it exists
        after = data.get('data', {}).get('after')
        if after:
            return count_words(subreddit, word_list, after, counts)

        if not counts:
            return

        # Once done, print the sorted results
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

    else:
        return

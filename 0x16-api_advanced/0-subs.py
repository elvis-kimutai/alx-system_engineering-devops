#!/usr/bin/python3
"""
    queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """retrive no of subscribers after quering subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:

        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0

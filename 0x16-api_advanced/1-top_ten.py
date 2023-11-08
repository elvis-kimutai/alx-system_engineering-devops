#!/usr/bin/python3
"""
    queries the Reddit API and prints the titles of the first
    10 hot posts
"""

import requests


def top_ten(subreddit):
    """queries Reddit and print titles of the first 10 hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            subb = response.json().get('data').get('subb')
            for i in range(10):
                print(subb[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
